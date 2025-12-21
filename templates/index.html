<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мои Заказы</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .nav {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .nav a {
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            text-decoration: none;
            transition: all 0.3s;
        }

        .nav a:hover {
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }

        .content {
            padding: 30px;
        }

        .info-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            text-align: center;
            font-size: 1.2em;
        }

        .form-section {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
        }

        .form-section h2 {
            color: #667eea;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        .form-group label {
            margin-bottom: 5px;
            color: #333;
            font-weight: 500;
            font-size: 0.9em;
        }

        .form-group input, .form-group select {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s;
        }

        .form-group input:focus, .form-group select:focus {
            outline: none;
            border-color: #667eea;
        }

        .form-group small {
            color: #6c757d;
            font-size: 0.85em;
            margin-top: 3px;
        }

        .checkbox-group {
            display: flex;
            gap: 20px;
            margin: 15px 0;
            flex-wrap: wrap;
        }

        .checkbox-group label {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
        }

        .checkbox-group input[type="checkbox"] {
            width: 20px;
            height: 20px;
            cursor: pointer;
        }

        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            font-weight: 600;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        }

        .btn-sm {
            padding: 8px 16px;
            font-size: 0.9em;
            width: auto;
        }

        .filters {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }

        .filters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .table-container {
            overflow-x: auto;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }

        thead {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        th {
            padding: 15px 10px;
            text-align: left;
            font-weight: 600;
            font-size: 0.9em;
        }

        td {
            padding: 15px 10px;
            border-bottom: 1px solid #e0e0e0;
            vertical-align: top;
        }

        tbody tr:hover {
            background: #f8f9fa;
        }

        .status-badge {
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
            display: inline-block;
        }

        .status-ordered { background: #fff3cd; color: #856404; }
        .status-in_china { background: #cce5ff; color: #004085; }
        .status-in_transit { background: #d1ecf1; color: #0c5460; }
        .status-received { background: #d4edda; color: #155724; }
        .status-sold { background: #d6d8db; color: #383d41; }

        .marketplace-badge {
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.8em;
            background: #e7f3ff;
            color: #0066cc;
            display: inline-block;
            margin-top: 3px;
        }

        .payment-status {
            font-size: 0.8em;
            margin-top: 5px;
        }

        .payment-paid {
            color: #28a745;
            font-weight: 600;
        }

        .payment-unpaid {
            color: #dc3545;
            font-weight: 600;
        }

        .product-image {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: 8px;
        }

        .action-btn {
            padding: 5px 12px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 0.85em;
            margin: 2px;
            display: inline-block;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-delete { 
            background: #dc3545; 
            color: white; 
        }

        .btn-delete:hover {
            background: #c82333;
        }

        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #6c757d;
        }

        .empty-state h3 {
            font-size: 1.5em;
            margin-bottom: 10px;
        }

        .autocomplete {
            position: relative;
        }

        .autocomplete-items {
            position: absolute;
            border: 1px solid #d4d4d4;
            border-top: none;
            z-index: 99;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            max-height: 200px;
            overflow-y: auto;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .autocomplete-items div {
            padding: 10px;
            cursor: pointer;
            border-bottom: 1px solid #e0e0e0;
        }

        .autocomplete-items div:hover {
            background-color: #667eea;
            color: white;
        }

        .debtor-warning {
            background: #fff3cd;
            color: #856404;
            padding: 3px 8px;
            border-radius: 5px;
            font-size: 0.8em;
            margin-left: 8px;
        }

        .status-form {
            background: #f8f9fa;
            padding: 12px;
            border-radius: 8px;
            margin-top: 8px;
        }

        .status-form select {
            width: 100%;
            padding: 8px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            margin-bottom: 8px;
            font-size: 0.9em;
        }

        .status-form input {
            width: 100%;
            padding: 8px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            margin-bottom: 8px;
            font-size: 0.9em;
        }

        .status-form .checkbox-item {
            display: flex;
            align-items: center;
            gap: 8px;
            margin: 5px 0;
            font-size: 0.85em;
        }

        .status-form .checkbox-item input {
            width: auto;
            margin: 0;
        }

        .status-fields {
            margin-top: 8px;
        }

        .product-link {
            color: #007bff;
            text-decoration: none;
            font-size: 0.85em;
            display: inline-block;
            margin-top: 3px;
        }

        .product-link:hover {
            text-decoration: underline;
        }

        .info-small {
            font-size: 0.8em;
            color: #6c757d;
            margin-top: 5px;
        }

        @media (max-width: 768px) {
            .form-grid {
                grid-template-columns: 1fr;
            }
            
            .filters-grid {
                grid-template-columns: 1fr;
            }

            th, td {
                padding: 8px 5px;
                font-size: 0.85em;
            }

            .product-image {
                width: 40px;
                height: 40px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📦 Мои Заказы</h1>
            <div class="nav">
                <a href="{{ url_for('dashboard') }}">📊 Главная</a>
                <a href="{{ url_for('index') }}">🛒 Заказы</a>
                <a href="{{ url_for('warehouse') }}">📦 Склад</a>
                <a href="{{ url_for('sales') }}">💰 Продажи</a>
                <a href="{{ url_for('customers') }}">👥 Клиенты</a>
                <a href="{{ url_for('logout') }}">🚪 Выход</a>
            </div>
        </div>

        <div class="content">
            <div class="info-box">
                💱 Курс: 1 CNY = {{ "%.2f"|format(current_rate) }} TJS
            </div>

            <div class="form-section">
                <h2>➕ Новый заказ</h2>
                <form method="POST" action="{{ url_for('add_product') }}">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>№ заказа</label>
                            <input type="text" name="order_number" required>
                        </div>
                        <div class="form-group">
                            <label>Название</label>
                            <input type="text" name="name" required>
                        </div>
                        <div class="form-group">
                            <label>Цена ¥</label>
                            <input type="number" step="0.01" name="price_cny" required>
                        </div>
                        <div class="form-group">
                            <label>Количество</label>
                            <input type="number" name="quantity" value="1" required>
                        </div>
                    </div>

                    <div class="form-grid">
                        <div class="form-group">
                            <label>🔗 Ссылка на товар</label>
                            <input type="url" name="product_url" placeholder="https://1688.com/...">
                            <small>Маркетплейс определится автоматически</small>
                        </div>
                        <div class="form-group">
                            <label>🖼️ Ссылка на фото</label>
                            <input type="url" name="product_image" placeholder="https://...">
                        </div>
                    </div>

                    <div class="form-grid">
                        <div class="form-group">
                            <label>Карго</label>
                            <input type="text" name="cargo">
                        </div>
                        <div class="form-group autocomplete">
                            <label>Клиент</label>
                            <input type="text" name="customer_name" id="customer_input" autocomplete="off">
                            <div id="autocomplete-list" class="autocomplete-items"></div>
                        </div>
                    </div>

                    <div class="checkbox-group">
                        <label>
                            <input type="checkbox" name="customer_paid_product">
                            ✅ Клиент оплатил товар
                        </label>
                        <label>
                            <input type="checkbox" name="customer_paid_shipping">
                            ✅ Клиент оплатил доставку
                        </label>
                    </div>

                    <button type="submit" class="btn">Добавить заказ</button>
                </form>
            </div>

            <div class="filters">
                <form method="GET">
                    <div class="filters-grid">
                        <input type="text" name="search" placeholder="🔍 Поиск..." value="{{ search_query }}" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px;">
                        
                        <select name="status" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px;">
                            <option value="">Все статусы</option>
                            <option value="ordered" {% if status_filter == 'ordered' %}selected{% endif %}>Заказан</option>
                            <option value="in_china" {% if status_filter == 'in_china' %}selected{% endif %}>В Китае</option>
                            <option value="in_transit" {% if status_filter == 'in_transit' %}selected{% endif %}>В пути</option>
                            <option value="received" {% if status_filter == 'received' %}selected{% endif %}>Получен</option>
                            <option value="sold" {% if status_filter == 'sold' %}selected{% endif %}>Продан</option>
                        </select>

                        <select name="marketplace" style="padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px;">
                            <option value="">Все маркетплейсы</option>
                            {% for marketplace in marketplaces %}
                            <option value="{{ marketplace }}" {% if marketplace_filter == marketplace %}selected{% endif %}>{{ marketplace }}</option>
                            {% endfor %}
                        </select>

                        <button type="submit" class="btn">Найти</button>
                    </div>
                </form>
            </div>

            <div class="table-container">
                {% if products %}
                <table>
                    <thead>
                        <tr>
                            <th style="width: 80px;">Фото</th>
                            <th style="width: 100px;">№ Заказа</th>
                            <th>Название</th>
                            <th style="width: 120px;">Цена</th>
                            <th style="width: 60px;">Кол-во</th>
                            <th style="width: 100px;">Клиент</th>
                            <th style="width: 300px;">Статус и управление</th>
                            <th style="width: 80px;">Действия</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for product in products %}
                        <tr>
                            <td>
                                {% if product.product_image %}
                                <img src="{{ product.product_image }}" class="product-image" alt="{{ product.name }}">
                                {% else %}
                                <div style="width: 60px; height: 60px; background: #f0f0f0; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 2em;">📦</div>
                                {% endif %}
                            </td>
                            <td><strong>{{ product.order_number }}</strong></td>
                            <td>
                                {{ product.name }}
                                {% if product.marketplace %}
                                <br><span class="marketplace-badge">{{ product.marketplace }}</span>
                                {% endif %}
                                {% if product.product_url %}
                                <br><a href="{{ product.product_url }}" target="_blank" class="product-link">🔗 Ссылка на товар</a>
                                {% endif %}
                            </td>
                            <td>
                                <strong>{{ "%.2f"|format(product.price_cny) }} ¥</strong>
                                <br>{{ "%.2f"|format(product.price_tjs) }} с
                            </td>
                            <td>{{ product.quantity }}</td>
                            <td>{{ product.customer_name or '-' }}</td>
                            <td>
                                <span class="status-badge status-{{ product.status }}">
                                    {% if product.status == 'ordered' %}Заказан
                                    {% elif product.status == 'in_china' %}В Китае
                                    {% elif product.status == 'in_transit' %}В пути
                                    {% elif product.status == 'received' %}Получен
                                    {% elif product.status == 'sold' %}Продан
                                    {% endif %}
                                </span>

                                <!-- Форма изменения статуса -->
                                <form method="POST" action="{{ url_for('update_status', product_id=product.id) }}" class="status-form">
                                    <select name="status" onchange="showStatusFields(this, {{ product.id }})">
                                        <option value="ordered" {% if product.status == 'ordered' %}selected{% endif %}>Заказан</option>
                                        <option value="in_china" {% if product.status == 'in_china' %}selected{% endif %}>В Китае</option>
                                        <option value="in_transit" {% if product.status == 'in_transit' %}selected{% endif %}>В пути</option>
                                        <option value="received" {% if product.status == 'received' %}selected{% endif %}>Получен</option>
                                    </select>
                                    
                                    <!-- Поля для "В пути" -->
                                    <div id="transit_{{ product.id }}" class="status-fields" style="display: {% if product.status == 'in_transit' %}block{% else %}none{% endif %};">
                                        <input type="text" name="track_code" placeholder="Трек-код" value="{{ product.track_code or '' }}">
                                    </div>
                                    
                                    <!-- Поля для "Получен" -->
                                    <div id="received_{{ product.id }}" class="status-fields" style="display: {% if product.status == 'received' %}block{% else %}none{% endif %};">
                                        <input type="number" step="0.01" name="shipping_price" placeholder="Цена доставки" value="{{ product.shipping_price or '' }}">
                                        <input type="number" step="0.01" name="weight" placeholder="Вес (кг)" value="{{ product.weight or '' }}">
                                        
                                        <div class="checkbox-item">
                                            <input type="checkbox" name="customer_paid_product" id="paid_prod_{{ product.id }}" {% if product.customer_paid_product %}checked{% endif %}>
                                            <label for="paid_prod_{{ product.id }}">Оплатил товар</label>
                                        </div>
                                        <div class="checkbox-item">
                                            <input type="checkbox" name="customer_paid_shipping" id="paid_ship_{{ product.id }}" {% if product.customer_paid_shipping %}checked{% endif %}>
                                            <label for="paid_ship_{{ product.id }}">Оплатил доставку</label>
                                        </div>
                                    </div>
                                    
                                    <button type="submit" class="btn btn-sm">Обновить</button>
                                </form>

                                <!-- Информация -->
                                <div class="info-small">
                                    {% if product.order_date %}
                                    📅 {{ product.order_date.strftime('%d.%m.%Y') }}
                                    {% endif %}
                                    {% if product.track_code and product.status == 'in_transit' %}
                                    <br>📮 {{ product.track_code }}
                                    {% endif %}
                                    {% if product.shipping_price and product.status == 'received' %}
                                    <br>🚚 Доставка: {{ "%.2f"|format(product.shipping_price) }} с
                                    {% endif %}
                                </div>

                                <!-- Статус оплаты -->
                                {% if product.customer_name %}
                                <div class="payment-status">
                                    Товар: <span class="{% if product.customer_paid_product %}payment-paid{% else %}payment-unpaid{% endif %}">
                                        {{ '✅' if product.customer_paid_product else '❌' }}
                                    </span>
                                    | Доставка: <span class="{% if product.customer_paid_shipping %}payment-paid{% else %}payment-unpaid{% endif %}">
                                        {{ '✅' if product.customer_paid_shipping else '❌' }}
                                    </span>
                                </div>
                                {% endif %}
                            </td>
                            <td>
                                <a href="{{ url_for('delete_product', product_id=product.id) }}" 
                                   onclick="return confirm('Удалить заказ?')" 
                                   class="action-btn btn-delete">🗑️</a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                {% else %}
                <div class="empty-state">
                    <h3>📦 Заказов пока нет</h3>
                    <p>Добавьте первый заказ используя форму выше</p>
                </div>
                {% endif %}
            </div>
        </div>
    </div>

    <script>
        // Автодополнение для клиентов
        const customerInput = document.getElementById('customer_input');
        const autocompleteList = document.getElementById('autocomplete-list');
        const customers = {{ customers | tojson }};

        customerInput.addEventListener('input', function() {
            const val = this.value;
            autocompleteList.innerHTML = '';
            
            if (!val) return;
            
            const matches = customers.filter(c => 
                c.name.toLowerCase().includes(val.toLowerCase())
            );
            
            matches.forEach(customer => {
                const div = document.createElement('div');
                div.innerHTML = customer.name;
                
                if (customer.is_debtor) {
                    div.innerHTML += ' <span class="debtor-warning">⚠️ Должник: ' + customer.debt_amount + ' с</span>';
                }
                
                div.addEventListener('click', function() {
                    customerInput.value = customer.name;
                    autocompleteList.innerHTML = '';
                });
                
                autocompleteList.appendChild(div);
            });
        });

        document.addEventListener('click', function(e) {
            if (e.target !== customerInput) {
                autocompleteList.innerHTML = '';
            }
        });

        // Показ/скрытие полей в зависимости от статуса
        function showStatusFields(select, productId) {
            const transitFields = document.getElementById('transit_' + productId);
            const receivedFields = document.getElementById('received_' + productId);
            
            transitFields.style.display = 'none';
            receivedFields.style.display = 'none';
            
            if (select.value === 'in_transit') {
                transitFields.style.display = 'block';
            } else if (select.value === 'received') {
                receivedFields.style.display = 'block';
            }
        }
    </script>
</body>
</html>