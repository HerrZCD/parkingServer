from flask import Flask, make_response, jsonify
from flask import request
from flask_cors import CORS
import json
import pymysql


# python -m flask --app server run --debug.
# need to open mysql before run this script.

db = pymysql.connect(host='localhost',
                     user='root',
                     password='Amawenfei421',
                     database='parking2')

cursor = db.cursor()


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route("/login", methods=['GET', 'POST'])
def HandleLogin():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    name = j_data['name'];
    password = j_data['password'];
    result_text = {"statusCode": 200, "status": "fail"};
    if name and password:
        try:
            sql = "SELECT * FROM users where name='"+name + "';";
            print(sql)
            cursor.execute(sql);
            result = cursor.fetchall();
            dbname, dbpassword, dbaccount, dbrole, balance = result[0];
            if dbpassword == password:
                result_text = {"statusCode": 200, "status": "success", "role": dbrole, "balance": balance}
            else:
                print("invalid password")
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/getSpots", methods=['GET', 'POST'])
def HandleGetSpots():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    name = j_data['name'];
    result_text = '';
    result_arr = [];
    if name:
        try:
            if name == 'ALLUSERNAMES':
                sql = "SELECT * FROM spots;"
            else:
                sql = "SELECT * FROM spots where owner='"+name + "';"
            print(sql);
            cursor.execute(sql);
            results = cursor.fetchall();
            for result in results:
                print(result);
                id, width, height, owner, location, user_time_start, user_time_end, price, lat, lng, likes = result;
                text = {"width": width, "height": height, "location": location, "price": price, "user_time_start": user_time_start, "user_time_end": user_time_end, "owner": owner, "id": id, "lat": lat, "lng": lng, "likes": likes};
                result_arr.append(text);
                result_text = {"statusCode": 200, "status": "success", "results": result_arr}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response



@app.route("/register", methods=['GET', 'POST'])
def HandleRegister():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);
    print(data)
    print(j_data)
    print(j_data['name'])
    print(j_data['password'])
    print(j_data['loginRole'])

    name = j_data['name'];
    password = j_data['password'];
    role = j_data['loginRole'];
    result_text = '';
    if name and password:
        try:
            sql = 'INSERT INTO users (name, account, password, role) values ("{name}", "", "{password}", "{role}");'.format(name=name, password=password, role=role);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/addspots", methods=['GET', 'POST'])
def HandleAddSpots():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    width = j_data['width'];
    height = j_data['height'];
    location = j_data['location'];
    owner = j_data['owner'];
    price = j_data['price'];
    user_time_start = j_data['user_time_start'];
    user_time_end = j_data['user_time_end'];
    lat = j_data['lat'];
    lng = j_data['lng'];
    result_text = {"statusCode": 200, "status": "fail"}

    if width and height and location and owner:
        try:
            sql = 'INSERT INTO spots (width, height, owner, location, price, user_time_start, user_time_end, lat, lng) values ("{width}", "{height}", "{owner}", "{location}", "{price}", "{user_time_start}", "{user_time_end}", "{lat}", "{lng}");'.format(width=width, height=height, owner=owner, location=location, price=price, user_time_start=user_time_start, user_time_end=user_time_end, lat=lat, lng=lng);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/createorder", methods=['GET', 'POST'])
def HandleCreateOrder():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    spot_id = j_data['spot_id'];
    location = j_data['location'];
    owner = j_data['owner'];
    user = j_data['user'];
    price = j_data['price'];
    user_time_start = j_data['user_time_start'];
    duration = j_data['duration'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id and spot_id and owner and price and user and duration:
        try:
            sql = 'INSERT INTO orders (spot_id, owner, user, location, price, user_time_start, duration) values ("{spot_id}", "{owner}", "{user}", \
            "{location}", "{price}", "{user_time_start}", "{duration}");'.format(spot_id=spot_id, owner=owner, user=user, location=location, \
            price=price, user_time_start=user_time_start, duration=duration);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/getorders", methods=['GET', 'POST'])
def HandleGetOrders():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    name = j_data['name'];
    role = j_data['role'];
    result_text = '';
    result_arr = [];
    if name:
        try:
            if name == 'ALLUSERNAMES':
                sql = "SELECT * FROM orders;"
            else:
                if role == 'User':
                    sql = "SELECT * FROM orders where user='"+name + "';"
                elif role == 'Owner':
                    sql = "SELECT * FROM orders where owner='"+name + "';"
            print(sql);
            cursor.execute(sql);
            results = cursor.fetchall();
            for result in results:
                print(result)
                id, spot_id, price, owner, user, location, user_time_start, duration, state = result;
                text = {"id": id, "spot_id": spot_id, "price": price, "owner": owner, "user": user, "location": location,\
                        "user_time_start": user_time_start, "duration": duration, "state": state};
                result_arr.append(text);
                result_text = {"statusCode": 200, "status": "success", "results": result_arr}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/getbalance", methods=['GET', 'POST'])
def HandleGetBalance():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    name = j_data['name'];
    if name:
        try:
            sql = "SELECT balance FROM users where name='"+name + "'";
            print(sql);
            cursor.execute(sql);
            results = cursor.fetchall();
            balance = results[0];
            result_text = {"statusCode": 200, "status": "success", "balance": balance}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/setBalance", methods=['GET', 'POST'])
def HandleSetBalance():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    user = j_data['user'];
    owner = j_data['owner'];
    money = j_data['money'];
    if user:
        try:
            sql = "SELECT balance FROM users where name='"+user + "';";
            print(sql);
            cursor.execute(sql);
            results = cursor.fetchall();
            balance, = results[0];
            new_balance = balance - int(money);
            sql = 'UPDATE users SET balance="{balance}" where name="{user}";'.format(balance=new_balance, user=user);
            print(sql)
            cursor.execute(sql);
            db.commit();
            sql = "SELECT balance FROM users where name='"+owner + "';";
            print(sql);
            cursor.execute(sql);
            results = cursor.fetchall();
            balance, = results[0];
            new_balance = balance + int(money * 0.9);
            sql = 'UPDATE users SET balance="{balance}" where name="{user}";'.format(balance=new_balance, user=owner);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success", "balance": balance}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/modifyspots", methods=['GET', 'POST'])
def HandleModifySpots():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    width = j_data['width'];
    height = j_data['height'];
    location = j_data['location'];
    owner = j_data['owner'];
    price = j_data['price'];
    id = j_data['id'];
    lat = j_data['lat'];
    lng = j_data['lng'];
    user_time_start = j_data['user_time_start'];
    user_time_end = j_data['user_time_end'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id:
        try:
            sql = 'UPDATE spots SET width="{width}", height="{height}", location="{location}", price="{price}", user_time_start="{user_time_start}", user_time_end="{user_time_end}", lat="{lat}", lng="{lng}" where id={id};'.format(width=width, height=height, owner=owner, location=location, price=price, user_time_start=user_time_start, user_time_end=user_time_end, id=id, lat=lat, lng=lng);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/changeorderstate", methods=['GET', 'POST'])
def HandleChangeOrderState():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    id = j_data['id'];
    state = j_data['state'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id:
        try:
            sql = 'UPDATE orders SET state="{state}" where id ="{id}";'.format(id=id, state=state);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/like", methods=['GET', 'POST'])
def HandleLike():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    id = j_data['id'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id:
        try:
            sql = "SELECT likes FROM spots where id='"+str(id) + "';";
            cursor.execute(sql);
            results = cursor.fetchall();
            likes, = results[0];
            if not likes:
                likes = 0;
            likes = likes + 1;
            sql = 'UPDATE spots SET likes="{likes}" where id ="{id}";'.format(id=str(id), likes=likes);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route("/deletespots", methods=['GET', 'POST'])
def HandleDeleteSpots():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    id = j_data['id'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id:
        try:
            sql = 'DELETE FROM spots where id={id};'.format(id=id);
            print(sql)
            cursor.execute(sql);
            db.commit();
            result_text = {"statusCode": 200, "status": "success"}
        except:
            result_text = {"statusCode": 200, "status": "fail"}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

def EnsureParkingSpotsTable():
    sql = '''
    CREATE TABLE IF NOT EXISTS `spots`(
   `id` INT AUTO_INCREMENT PRIMARY KEY,
   `spot_id `int,
   `width` INT NOT NULL,
   `height` INT NOT NULL,
   `owner` varchar(100) NOT NULL,
   `location` varchar(100) NOT NULL,
   `user_time_start` varchar(30),
   `user_time_end` varchar(30),
   `price` INT,
   `lat` DOUBLE,
   `lng` DOUBLE,
   `likes` int default "0"
    )
    '''
    cursor.execute(sql);

def EnsureUserTable():
    sql = '''
    CREATE TABLE IF NOT EXISTS `users`(
   `name` varchar(100) PRIMARY KEY,
   `password` varchar(20),
   `account` varchar(100),
   `role` varchar(20),
   `balance` int default "1000"
    )
    '''
    cursor.execute(sql);

def EnsureOrderTable():
    sql = '''
    CREATE TABLE IF NOT EXISTS `orders`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `spot_id` INT NOT NULL,
    `price` INT NOT NULL,
    `owner` varchar(100) NOT NULL,
    `user` varchar(100) NOT NULL,
    `location` varchar(100) NOT NULL,
    `user_time_start` varchar(30),
    `duration` INT,
    `state` varchar(20) default "unconfirm"
    )
    '''
    cursor.execute(sql);

EnsureUserTable();
EnsureParkingSpotsTable();
EnsureOrderTable();


 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()