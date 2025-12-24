import os
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import requests
from sqlalchemy import func
from urllib.parse import urlparse
import cloudinary
import cloudinary.uploader

# Создаем приложение
app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
            )

# Конфигурация
app.secret_key = 'madalizoda-secret-key-2024-business-app'

# Определяем базу данных (PostgreSQL для продакшн, SQLite для локальной разработки)
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # Render использует postgres://, заменяем на postgresql+pg8000://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql+pg8000://', 1)
    elif database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgresql+pg8000://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Для локальной разработки
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'business.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Конфигурация Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', 'deaxtqh2w'),
    api_key=os.environ.get('CLOUDINARY_API_KEY', '874589763492562'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', 'Xf3uUJqrspJrhKW89BBWwerz1GI')
)

# Данные для аутентификации
USERNAME = 'Madalizoda'
PASSWORD_HASH = generate_password_hash('Madaliev_2008')


# Декоратор для защиты маршрутов
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


# Модель для товаров
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price_cny = db.Column(db.Float, nullable=False)
    price_tjs = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    status = db.Column(db.String(50), default='ordered')
    cargo = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    track_code = db.Column(db.String(100))
    shipping_price = db.Column(db.Float, default=0.0)
    weight = db.Column(db.Float)

    # Новые поля
    product_url = db.Column(db.String(500))  # Ссылка на товар
    product_image = db.Column(db.String(500))  # Ссылка на фото
    marketplace = db.Column(db.String(50))  # Название маркетплейса

    # Улучшенное отслеживание
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    shipping_date = db.Column(db.DateTime)
    receive_date = db.Column(db.DateTime)

    # Система оплат
    customer_paid_product = db.Column(db.Boolean, default=False)
    customer_paid_shipping = db.Column(db.Boolean, default=False)
    customer_bought = db.Column(db.Boolean, default=False)
    shipping_payment_amount = db.Column(db.Float, default=0.0)  # Сумма оплаты доставки клиентом

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.order_number} - {self.name}>'


# Модель для клиентов
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    city = db.Column(db.String(100))

    # Новые поля для должников
    debt_amount = db.Column(db.Float, default=0.0)  # Сумма долга
    is_debtor = db.Column(db.Boolean, default=False)  # Является должником
    notes = db.Column(db.Text)  # Заметки о клиенте

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Связь с продажами
    sales = db.relationship('Sale', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.name}>'


# Модель для продаж
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Связи
    product = db.relationship('Product', backref='sales')


# Модель для расходов
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Создание таблиц
with app.app_context():
    db.create_all()


# Функция для определения маркетплейса по URL
def detect_marketplace(url):
    if not url:
        return 'Неизвестно'

    url_lower = url.lower()

    if 'pinduoduo' in url_lower or 'pdd' in url_lower:
        return 'Pinduoduo'
    elif '1688.com' in url_lower:
        return '1688'
    elif 'poizon' in url_lower or 'dewu' in url_lower:
        return 'Poizon'
    elif 'taobao' in url_lower:
        return 'Taobao'
    elif 'wildberries' in url_lower or 'wb.ru' in url_lower:
        return 'Wildberries'
    elif 'tmall' in url_lower:
        return 'Tmall'
    elif 'aliexpress' in url_lower:
        return 'AliExpress'
    elif 'amazon' in url_lower:
        return 'Amazon'
    else:
        return 'Другой'


# Функция для расчета курса
def get_exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/CNY')
        data = response.json()
        return data['rates']['TJS']
    except:
        return 1.50  # fallback rate


# Функция для расчета себестоимости
def calculate_cost_price(product):
    return (product.price_tjs or 0) + (product.shipping_price or 0)


# Маршрут для входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Неверный логин или пароль')

    return render_template('login.html')


# Маршрут для выхода
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# Главная страница - дашборд
@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    # Получаем статистику
    total_products = Product.query.count()
    total_customers = Customer.query.count()

    # Статистика продаж
    sales_data = db.session.query(
        func.count(Sale.id),
        func.sum(Sale.sale_price),
        func.sum(Sale.sale_price - (Product.price_tjs + (Product.shipping_price or 0)))
    ).join(Sale.product).first()

    total_sales_count = sales_data[0] or 0
    total_revenue = sales_data[1] or 0
    total_profit = sales_data[2] or 0

    # Статистика по статусам
    status_stats = {
        'ordered': Product.query.filter_by(status='ordered').count(),
        'in_china': Product.query.filter_by(status='in_china').count(),
        'in_transit': Product.query.filter_by(status='in_transit').count(),
        'received': Product.query.filter_by(status='received').count(),
        'sold': Product.query.filter_by(status='sold').count()
    }

    # Популярные товары
    popular_products = db.session.query(
        Product.name,
        func.count(Sale.id).label('sales_count')
    ).join(Sale.product).group_by(Product.id).order_by(func.count(Sale.id).desc()).limit(5).all()

    # Общие расходы
    total_shipping = db.session.query(func.sum(Product.shipping_price)).scalar() or 0
    total_investment = db.session.query(func.sum(Product.price_tjs)).scalar() or 0

    # Количество должников
    debtors_count = Customer.query.filter_by(is_debtor=True).count()
    total_debt = db.session.query(func.sum(Customer.debt_amount)).filter(Customer.is_debtor == True).scalar() or 0

    stats = {
        'total_products': total_products,
        'total_customers': total_customers,
        'total_sales_count': total_sales_count,
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'status_stats': status_stats,
        'popular_products': popular_products,
        'total_shipping': total_shipping,
        'total_investment': total_investment,
        'debtors_count': debtors_count,
        'total_debt': total_debt
    }

    return render_template('dashboard.html', stats=stats)


# Страница заказов
@app.route('/orders')
@login_required
def index():
    current_rate = get_exchange_rate()

    # Получаем параметры поиска и сортировки
    search_query = request.args.get('search', '')
    status_filter = request.args.get('status', '')
    marketplace_filter = request.args.get('marketplace', '')
    sort_by = request.args.get('sort', 'created_at')
    sort_order = request.args.get('order', 'desc')

    # Базовый запрос
    query = Product.query

    # Применяем поиск
    if search_query:
        query = query.filter(
            db.or_(
                Product.order_number.ilike(f'%{search_query}%'),
                Product.name.ilike(f'%{search_query}%'),
                Product.customer_name.ilike(f'%{search_query}%')
            )
        )

    # Применяем фильтр по статусу
    if status_filter:
        query = query.filter(Product.status == status_filter)

    # Применяем фильтр по маркетплейсу
    if marketplace_filter:
        query = query.filter(Product.marketplace == marketplace_filter)

    # Применяем сортировку
    if sort_by == 'order_number':
        order_column = Product.order_number
    elif sort_by == 'name':
        order_column = Product.name
    elif sort_by == 'price':
        order_column = Product.price_tjs
    elif sort_by == 'status':
        order_column = Product.status
    elif sort_by == 'customer':
        order_column = Product.customer_name
    else:  # created_at по умолчанию
        order_column = Product.created_at

    # Порядок сортировки
    if sort_order == 'asc':
        query = query.order_by(order_column.asc())
    else:
        query = query.order_by(order_column.desc())

    products = query.all()

    # Обновляем цены в TJS если нужно
    for product in products:
        if not product.price_tjs:
            product.price_tjs = product.price_cny * current_rate
            db.session.commit()

    # Получаем список маркетплейсов для фильтра
    marketplaces = db.session.query(Product.marketplace).filter(Product.marketplace != None).distinct().all()
    marketplaces = [m[0] for m in marketplaces if m[0]]

    # Получаем всех клиентов для автодополнения
    customers_query = Customer.query.all()
    customers = [{'id': c.id, 'name': c.name, 'is_debtor': c.is_debtor, 'debt_amount': c.debt_amount or 0} for c in customers_query]

    return render_template('index.html',
                           products=products,
                           current_rate=current_rate,
                           search_query=search_query,
                           status_filter=status_filter,
                           marketplace_filter=marketplace_filter,
                           marketplaces=marketplaces,
                           sort_by=sort_by,
                           sort_order=sort_order,
                           customers=customers)

# Добавление товара
@app.route('/add_product', methods=['POST'])
@login_required
def add_product():
    current_rate = get_exchange_rate()
    
    # Получаем URL товара и определяем маркетплейс
    product_url = request.form.get('product_url', '')
    marketplace = detect_marketplace(product_url)
    
    # Обработка загрузки фото
    product_image_url = ''
    if 'product_image_file' in request.files:
        file = request.files['product_image_file']
        if file and file.filename:
            try:
                # Загружаем на Cloudinary
                upload_result = cloudinary.uploader.upload(file, folder="business_products")
                product_image_url = upload_result['secure_url']
            except Exception as e:
                print(f"Ошибка загрузки на Cloudinary: {e}")
    
    # Если не загрузили файл, проверяем ссылку
    if not product_image_url:
        product_image_url = request.form.get('product_image', '')
    
    # Получаем или создаем клиента
    customer_name = request.form.get('customer_name', '')
    customer = None
    if customer_name:
        customer = Customer.query.filter_by(name=customer_name).first()
        if not customer:
            customer = Customer(name=customer_name)
            db.session.add(customer)
            db.session.commit()

    # Получаем дату заказа (если указана, иначе текущая)
    order_date_str = request.form.get('order_date', '')
    if order_date_str:
        order_date = datetime.strptime(order_date_str, '%Y-%m-%d')
    else:
        order_date = datetime.utcnow()

    product = Product(
        order_number=request.form['order_number'],
        name=request.form['name'],
        price_cny=float(request.form['price_cny']),
        price_tjs=float(request.form['price_cny']) * current_rate,
        quantity=int(request.form['quantity']),
        cargo=request.form.get('cargo', ''),
        customer_name=customer_name,
        product_url=product_url,
        product_image=product_image_url,
        marketplace=marketplace,
        customer_paid_product='customer_paid_product' in request.form,
        customer_paid_shipping='customer_paid_shipping' in request.form,
        shipping_payment_amount=float(request.form.get('shipping_payment_amount', 0) or 0),
        order_date=order_date
    )
    
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('index'))



# Обновление статуса товара
@app.route('/update_status/<int:product_id>', methods=['POST'])
@login_required
def update_status(product_id):
    product = Product.query.get_or_404(product_id)
    new_status = request.form['status']
    old_status = product.status
    product.status = new_status

    # Обновляем даты в зависимости от статуса
    if new_status == 'ordered' and not product.order_date:
        product.order_date = datetime.utcnow()

    elif new_status == 'in_china' and old_status == 'ordered':
        pass

    elif new_status == 'in_transit':
    # Дата отправки (если указана, иначе текущая)
        shipping_date_str = request.form.get('shipping_date', '')
    if shipping_date_str:
        product.shipping_date = datetime.strptime(shipping_date_str, '%Y-%m-%d')
    else:
        product.shipping_date = datetime.utcnow()
    if request.form.get('track_code'):
        product.track_code = request.form['track_code']

    elif new_status == 'received':
    # Дата получения (если указана, иначе текущая)
        receive_date_str = request.form.get('receive_date', '')
    if receive_date_str:
        product.receive_date = datetime.strptime(receive_date_str, '%Y-%m-%d')
    else:
        product.receive_date = datetime.utcnow()
    if request.form.get('shipping_price'):
        product.shipping_price = float(request.form['shipping_price'])
    if request.form.get('weight'):
        product.weight = float(request.form['weight'])

    product.customer_paid_product = 'customer_paid_product' in request.form
    product.customer_paid_shipping = 'customer_paid_shipping' in request.form
    if request.form.get('shipping_payment_amount'):
        product.shipping_payment_amount = float(request.form['shipping_payment_amount'])
    db.session.commit()
    return redirect(url_for('index'))


# Страница склада
@app.route('/warehouse')
@login_required
def warehouse():
    # Получаем параметры поиска и сортировки
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', 'receive_date')
    sort_order = request.args.get('order', 'desc')

    # Базовый запрос - только товары со статусом 'received'
    query = Product.query.filter_by(status='received')

    # Применяем поиск
    if search_query:
        query = query.filter(
            db.or_(
                Product.order_number.ilike(f'%{search_query}%'),
                Product.name.ilike(f'%{search_query}%'),
                Product.customer_name.ilike(f'%{search_query}%')
            )
        )

    # Применяем сортировку
    if sort_by == 'order_number':
        query = query.order_by(Product.order_number.asc() if sort_order == 'asc' else Product.order_number.desc())
    elif sort_by == 'name':
        query = query.order_by(Product.name.asc() if sort_order == 'asc' else Product.name.desc())
    elif sort_by == 'cost':
        products = query.all()
        products.sort(key=lambda x: (x.price_tjs or 0) + (x.shipping_price or 0),
                      reverse=(sort_order == 'desc'))
        return render_template('warehouse.html',
                               products=products,
                               search_query=search_query,
                               sort_by=sort_by,
                               sort_order=sort_order)
    elif sort_by == 'quantity':
        query = query.order_by(Product.quantity.asc() if sort_order == 'asc' else Product.quantity.desc())
    else:  # receive_date по умолчанию
        query = query.order_by(Product.receive_date.asc() if sort_order == 'asc' else Product.receive_date.desc())

    products = query.all()

    return render_template('warehouse.html',
                           products=products,
                           search_query=search_query,
                           sort_by=sort_by,
                           sort_order=sort_order)


# Добавление продажи
@app.route('/add_sale', methods=['POST'])
@login_required
def add_sale():
    product_id = request.form['product_id']
    customer_name = request.form['customer_name']
    sale_price = float(request.form['sale_price'])

    # Находим или создаем клиента
    customer = Customer.query.filter_by(name=customer_name).first()
    if not customer:
        customer = Customer(name=customer_name)
        db.session.add(customer)
        db.session.commit()

    # Создаем продажу
    product = Product.query.get(product_id)
    sale = Sale(
        product_id=product_id,
        customer_id=customer.id,
        sale_price=sale_price
    )

    # Обновляем статус товара
    product.status = 'sold'

    db.session.add(sale)
    db.session.commit()
    return redirect(url_for('warehouse'))


# Страница продаж
@app.route('/sales')
@login_required
def sales():
    search_query = request.args.get('search', '')
    date_filter = request.args.get('date', '')
    sort_by = request.args.get('sort', 'sale_date')
    sort_order = request.args.get('order', 'desc')

    query = Sale.query

    if search_query:
        query = query.join(Product).join(Customer).filter(
            db.or_(
                Product.name.ilike(f'%{search_query}%'),
                Product.order_number.ilike(f'%{search_query}%'),
                Customer.name.ilike(f'%{search_query}%')
            )
        )

    if date_filter:
        try:
            filter_date = datetime.strptime(date_filter, '%Y-%m-%d')
            next_day = filter_date + timedelta(days=1)
            query = query.filter(Sale.sale_date >= filter_date, Sale.sale_date < next_day)
        except ValueError:
            pass

    if sort_by == 'product':
        query = query.join(Product).order_by(Product.name.asc() if sort_order == 'asc' else Product.name.desc())
    elif sort_by == 'customer':
        query = query.join(Customer).order_by(Customer.name.asc() if sort_order == 'asc' else Customer.name.desc())
    elif sort_by == 'price':
        query = query.order_by(Sale.sale_price.asc() if sort_order == 'asc' else Sale.sale_price.desc())
    elif sort_by == 'profit':
        sales_list = query.all()
        for sale in sales_list:
            sale.profit = sale.sale_price - calculate_cost_price(sale.product)

        sales_list.sort(key=lambda x: x.profit, reverse=(sort_order == 'desc'))
        total_revenue = sum(sale.sale_price for sale in sales_list)
        total_profit = sum(sale.profit for sale in sales_list)

        return render_template('sales.html',
                               sales=sales_list,
                               total_revenue=total_revenue,
                               total_profit=total_profit,
                               calculate_cost_price=calculate_cost_price,
                               search_query=search_query,
                               date_filter=date_filter,
                               sort_by=sort_by,
                               sort_order=sort_order)
    else:
        query = query.order_by(Sale.sale_date.asc() if sort_order == 'asc' else Sale.sale_date.desc())

    sales_list = query.all()

    for sale in sales_list:
        sale.profit = sale.sale_price - calculate_cost_price(sale.product)

    total_revenue = sum(sale.sale_price for sale in sales_list)
    total_profit = sum(sale.profit for sale in sales_list)

    return render_template('sales.html',
                           sales=sales_list,
                           total_revenue=total_revenue,
                           total_profit=total_profit,
                           calculate_cost_price=calculate_cost_price,
                           search_query=search_query,
                           date_filter=date_filter,
                           sort_by=sort_by,
                           sort_order=sort_order)


# Страница клиентов
@app.route('/customers')
@login_required
def customers():
    search_query = request.args.get('search', '')
    city_filter = request.args.get('city', '')
    debtor_filter = request.args.get('debtor', '')
    sort_by = request.args.get('sort', 'name')
    sort_order = request.args.get('order', 'asc')

    query = Customer.query

    if search_query:
        query = query.filter(
            db.or_(
                Customer.name.ilike(f'%{search_query}%'),
                Customer.phone.ilike(f'%{search_query}%'),
                Customer.city.ilike(f'%{search_query}%')
            )
        )

    if city_filter:
        query = query.filter(Customer.city.ilike(f'%{city_filter}%'))

    if debtor_filter == 'yes':
        query = query.filter(Customer.is_debtor == True)
    elif debtor_filter == 'no':
        query = query.filter(Customer.is_debtor == False)

    all_customers = query.all()

    for customer in all_customers:
        customer_sales = Sale.query.filter_by(customer_id=customer.id).all()
        customer.total_orders = len(customer_sales)
        customer.total_sales = sum(sale.sale_price for sale in customer_sales)
        customer.total_profit = sum(sale.sale_price - calculate_cost_price(sale.product) for sale in customer_sales)

    if sort_by == 'name':
        all_customers.sort(key=lambda x: x.name or '', reverse=(sort_order == 'desc'))
    elif sort_by == 'orders':
        all_customers.sort(key=lambda x: x.total_orders, reverse=(sort_order == 'desc'))
    elif sort_by == 'sales':
        all_customers.sort(key=lambda x: x.total_sales, reverse=(sort_order == 'desc'))
    elif sort_by == 'profit':
        all_customers.sort(key=lambda x: x.total_profit, reverse=(sort_order == 'desc'))
    elif sort_by == 'city':
        all_customers.sort(key=lambda x: x.city or '', reverse=(sort_order == 'desc'))
    elif sort_by == 'debt':
        all_customers.sort(key=lambda x: x.debt_amount or 0, reverse=(sort_order == 'desc'))

    cities = db.session.query(Customer.city).filter(Customer.city != None).filter(Customer.city != '').distinct().all()
    cities = [city[0] for city in cities if city[0]]

    return render_template('customers.html',
                           customers=all_customers,
                           cities=cities,
                           search_query=search_query,
                           city_filter=city_filter,
                           debtor_filter=debtor_filter,
                           sort_by=sort_by,
                           sort_order=sort_order)


# Детальная страница клиента
@app.route('/customer/<int:customer_id>')
@login_required
def customer_detail(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    customer_sales = Sale.query.filter_by(customer_id=customer.id).order_by(Sale.sale_date.desc()).all()

    stats = {
        'total_orders': len(customer_sales),
        'total_sales': sum(sale.sale_price for sale in customer_sales),
        'total_profit': sum(sale.sale_price - calculate_cost_price(sale.product) for sale in customer_sales)
    }

    return render_template('customer_detail.html', customer=customer, stats=stats,
                           calculate_cost_price=calculate_cost_price, sales=customer_sales)


# Добавление клиента
@app.route('/add_customer', methods=['POST'])
@login_required
def add_customer():
    customer = Customer(
        name=request.form['name'],
        phone=request.form.get('phone', ''),
        city=request.form.get('city', ''),
        notes=request.form.get('notes', '')
    )

    db.session.add(customer)
    db.session.commit()
    return redirect(url_for('customers'))


# Обновление информации о клиенте (долг)
@app.route('/update_customer/<int:customer_id>', methods=['POST'])
@login_required
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    customer.name = request.form.get('name', customer.name)
    customer.phone = request.form.get('phone', customer.phone)
    customer.city = request.form.get('city', customer.city)
    customer.notes = request.form.get('notes', customer.notes)

    debt_amount = request.form.get('debt_amount', 0)
    customer.debt_amount = float(debt_amount) if debt_amount else 0
    customer.is_debtor = customer.debt_amount > 0

    db.session.commit()
    return redirect(url_for('customer_detail', customer_id=customer_id))


# Добавление расхода
@app.route('/add_expense', methods=['POST'])
@login_required
def add_expense():
    expense = Expense(
        description=request.form['description'],
        amount=float(request.form['amount']),
        category=request.form['category']
    )

    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('dashboard'))


# Удаление товара
@app.route('/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))


# Удаление клиента
@app.route('/delete_customer/<int:customer_id>')
@login_required
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers'))


# Возврат товара
@app.route('/return_sale/<int:sale_id>')
@login_required
def return_sale(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    product = sale.product

    product.status = 'received'

    db.session.delete(sale)
    db.session.commit()

    return redirect(url_for('sales'))


# Удаление продажи
@app.route('/delete_sale/<int:sale_id>')
@login_required
def delete_sale(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for('sales'))


# API для автодополнения клиентов
@app.route('/api/customers/search')
@login_required
def search_customers():
    query = request.args.get('q', '')
    if query:
        customers = Customer.query.filter(
            Customer.name.ilike(f'%{query}%')
        ).limit(10).all()
        results = [{'id': customer.id, 'name': customer.name, 'is_debtor': customer.is_debtor, 'debt_amount': customer.debt_amount} for customer in customers]
    else:
        results = []

    return jsonify(results)


# Автоматическое создание базы при запуске
def init_db():
    with app.app_context():
        db.create_all()
        print("✅ База данных создана/проверена")


# Вызываем при импорте
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)