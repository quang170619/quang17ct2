from flask import Flask, jsonify, request
import os
import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv('db_ip') #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'giuaki'

@app.route('/')
def hello():    
    #return 'this is backend'
    c1 = bo.Customer(1, 'Kien Truc', 'HeryPoster', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    return c1.CustomerName

@app.route('/customer_insert')
def test_insert():
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1, 'Ha', 'Nguyen', 'Hoa cam', 'Danang', '50000', 'Vietnam')
    s1 = c2.insert(c1)
    return s1  
    #them du lieu customers
@app.route('/user/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'],
                            data['CustomerName'],
                            data['ContactName'], 
                            data['Address'], 
                            data['City'], 
                            data['PostalCode'], 
                            data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/test_send_receive', methods=['POST'])
def test_send_receive():
    x = request.json['x']
    y = x + 1
    result = {}
    result['y'] = y
    return jsonify(result), 200

#Hien thi tat ca cac du lieu
@app.route('/customer/all_Customer')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200
# Delete customer
@app.route('/customer/delete/<int:customer_id>' , methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customer(CustomerID = customer_id)
    result = do.Customer(ConnectionData).delete(c)
    return jsonify({'message': result[0]}),result[1]
#  Update customer
@app.route('/customer/update/<int:customer_id>' , methods=['PUT'])
def update_coustomer(customer_id):
    data = request.json
    c = bo.Customer(CustomerID =  customer_id , CustomerName=data['CustomerName'], ContactName=data['ContactName'], Address=data['Address'], City = data['City'],  PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customer(ConnectionData).update(c)
    return jsonify({'message': result[0]}),result[1]
    
#Show some row by ID
# CUSTOMER
@app.route('/customer/get/<int:customer_id>')
def get_user_by_id(user_id):
    c = bo.Customer(CustomerID = user_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200
#--------------------------------------------------------------------------
# Categories
@app.route('/categories_insert')
def test_insertca():
    c2 = do.Categories(ConnectionData)
    c1 = bo.Categories(1 , 'drink' , 'soft drinks, cafe, milk')
    s1 = c2.insert(c1)
    return s1

@app.route('/categories/all')
def get_all_categories():
    result = do.Categories(ConnectionData).get_all()
    return jsonify(result), 200
@app.route('/categories/get/<int:categories_id>')
def get_categories_by_id(categories_id):
    c = bo.Customer(CategoryID=categories_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200
@app.route('/categories/update/<int:categories_id>', methods=['PUT'])
def update_categories_by_id(categories_id):
    data = request.json
    c = bo.Employees(CategoryID=CategoryID, CategoryName=data['CategoryName'], Description=data['Description'])
    result = do.Employees(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/categories/delete/<int:categories_id>', methods=['DELETE'])
def delete_categories_by_id(categories_id):
    c = bo.Categories(CategoryID=categories_id)
    result = do.Employees(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
#*********************************
@app.route('/user/get_by_id', methods=['POST'])
def user_get_by_id():
    user_id = request.json['user_id']
    result = {}
    result['user_id'] = 1
    return jsonify(result), 200
# Employees -----------------------------------------
@app.route('/employees/insert', methods=['POST'])
def insert_employees():
    data = request.json
    c1 = bo.Employees(EmployeeID=data['EmployeeID'],
                         LastName=data['LastName'],
                          FirstName=data['FirstName'],
                           BirthDate=data['BirthDate'],
                            Photo=data['Photo'],
                              Notes=data['Notes'])
    c2 = do.Employees(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200
@app.route('/employees/all')
def get_all_employees():
    result = do.Employees(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/employees/get/<int:employees_id>')
def get_employees_by_id(employees_id):
    c = bo.Employees(EmployeeID=employees_id)
    result = do.Employees(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/employees/update/<int:employees_id>', methods=['PUT'])
def update_employees_by_id(employees_id):
    data = request.json
    c = bo.Employees(EmployeeID=EmployeeID, LastName=data['LastName'], FirstName=data['FirstName'], BirthDate=data['BirthDate'], Photo=data['Photo'],  Notes=data['Notes'])
    result = do.Employees(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/employees/delete/<int:employees_id>', methods=['DELETE'])
def delete_employees_by_id(employees_id):
    c = bo.Employees(EmployeeID=employees_id)
    result = do.Employees(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
# OrderDetails ----------------------------------------------------------------------
@app.route('/orderdetails/insert', methods=['POST'])
def orderdetails_insert():
    data = request.json
    c1 = bo.OrderDetails(OrderDetailID=data['OrderDetailID'],
                                 OrderID=data['OrderID'],
                                  ProductID=data['ProductID'],
                                   Quantity=data['Quantity'])
    c2 = do.OrderDetails(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/orderdetails/all')
def get_all_orderdetails():
    result = do.OrderDetails(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/orderdetails/get/<int:orderdetails_id>')
def get_orderdetails_by_id(orderdetails_id):
    c = bo.OrderDetails(OrderDetailID=orderdetails_id)
    result = do.OrderDetails(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/orderdetails/update/<int:orderdetails_id>', methods=['PUT'])
def update_orderdetails_by_id(orderdetails_id):
    data = request.json
    c = bo.OrderDetails(OrderDetailID=OrderDetailID, OrderID=data['OrderID'], ProductID=data['ProductID'], Quantity=data['Quantity'])
    result = do.OrderDetails(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/orderdetails/delete/<int:orderdetails_id>', methods=['DELETE'])
def delete_orderdetails_by_id(orderdetails_id):
    c = bo.OrderDetails(OrderDetailID=orderdetails_id)
    result = do.OrderDetails(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
# Orders ----------------------------------------------------------------------
@app.route('/orders/insert', methods=['POST'])
def orders_insert():
    data = request.json
    c1 = bo.Orders(OrderID=data['OrderID'],
             CustomerID=data['CustomerID'],
              EmployeeID=data['EmployeeID'],
               OrderDate=data['OrderDate'],
                ShipperID=data['ShipperID'])
    c2 = do.Orders(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/orders/all')
def get_all_ordersr():
    result = do.Orders(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/orders/get/<int:orders_id>')
def get_orders_by_id(orders_id):
    c = bo.Orders(OrderID=orders_id)
    result = do.Orders(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/orders/update/<int:orders_id>', methods=['PUT'])
def update_orders_by_id(supplier_id):
    data = request.json
    c = bo.Orders(OrderID=OrderID, CustomerID=data['CustomerID'], EmployeeID=data['EmployeeID'], OrderDate=data['OrderDate'], ShipperID=data['ShipperID'])
    result = do.Orders(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/orders/delete/<int:orders_id>', methods=['DELETE'])
def delete_orders_by_id(orders_id):
    c = bo.Orders(OrderID=orders_id)
    result = do.Orders(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
# Shipper API ----------------------------------------------------------------------
@app.route('/shipper/insert', methods=['POST'])
def insert_shipper():
    data = request.json
    shipper = bo.Shippers(ShipperID=data['ShipperID'],
                        ShipperName=data['ShipperName'],
                         Phone=data['Phone'])
    result = do.Shippers(ConnectionData).insert(shipper)
    return jsonify({'message': result}), 200

@app.route('/shipper/all')
def get_all_shipper():
    c = do.Shippers(ConnectionData).get_all()
    return jsonify(c), 200

@app.route('/shipper/get/<int:shipper_id>')
def get_shipper_by_id(shipper_id):
    shipper = bo.Shippers(shipper_id=shipper_id)
    result = do.Shippers(ConnectionData).get_by_id(shipper)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/shipper/update/<int:shipper_id>', methods=['PUT'])
def update_shipper_by_id(shipper_id):
    data = request.json
    shipper = bo.Shippers(shipper_id=shipper_id, shipper_name=data['shipper_name'], phone=data['phone'])
    result = do.Shippers(ConnectionData).update(shipper)
    return jsonify({'message': result[0]}), result[1]

@app.route('/shipper/delete/<int:shipper_id>', methods=['DELETE'])
def delete_shipper_by_id(shipper_id):
    c = bo.Shipper(shipper_id=shipper_id)
    result = do.Shippers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

# Supplier----------------------------------------------------------------------------------------

@app.route('/supplier/insert', methods=['POST'])
def supplier_insert():
    data = request.json
    c1 = bo.Suppliers(SupplierID=data['SupplierID'],
                    SupplierName=data['SupplierName'],
                         ContactName=data['ContactName'],
                          Address=data['Address'], City=data['City'],
                           PostalCode=data['PostalCode'], 
                           Country=data['Country'],
                            Phone=data['Phone'])
    c2 = do.Suppliers(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/supplier/all')
def get_all_supplier():
    result = do.Suppliers(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/supplier/get/<int:supplier_id>')
def get_supplier_by_id(supplier_id):
    c = bo.Suppliers(SupplierID=supplier_id)
    result = do.Suppliers(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/supplier/update/<int:supplier_id>', methods=['PUT'])
def update_supplier_by_id(supplier_id):
    data = request.json
    c = bo.Suppliers(SupplierID=supplier_id, SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    result = do.Suppliers(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/supplier/delete/<int:supplier_id>', methods=['DELETE'])
def delete_supplier_by_id(supplier_id):
    c = bo.Supplier(SupplierID=supplier_id)
    result = do.Supplier(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]
    
# Products: --------------------------------------------------------------------------------------
@app.route('/product/insert', methods=['POST'])
def product_insert():
    data = request.json
    c1 = bo.Products(ProductID=data['ProductID'],
                             product_name=data['product_name'],
                                 unit=data['Unit'],
                                  price=data['price'],
                                   supplier_id=data['supplier_id'],
                                    category_id=data['category_id'])
    c2 = do.Products(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/product/all')
def get_all_product():
    result = do.Products(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/product/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(product_id):
    if request.method == 'GET':
        # Get a product
        c = bo.Products(product_id=product_id)
        result = do.Products(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update a product
        data = request.json
        c = bo.Products(product_id=product_id, product_name=data['product_name'], unit=data['unit'], price=data['price'], supplier_id=data['supplier_id'], category_id=data['category_id'])
        result = do.Products(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete a product
        c = bo.Products(product_id=product_id)
        result = do.Products(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    