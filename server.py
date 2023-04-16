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
                     database='parking')

cursor = db.cursor()


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route("/login", methods=['GET', 'POST'])
def HandleLogin():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);

    name = j_data['name'];
    password = j_data['password'];
    result_text = '';
    if name and password:
        try:
            sql = "SELECT * FROM users where name='"+name + "'";
            cursor.execute(sql);
            result = cursor.fetchall();
            dbname, dbaccount, dbpassword, dbrole = result[0];
            if dbpassword == password:
                result_text = {"statusCode": 200, "status": "success", "role": dbrole}
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
                width, height, location, price, user_time_start, user_time_end, owner, id = result;
                text = {"width": width, "height": height, "location": location, "price": price, "user_time_start": user_time_start, "user_time_end": user_time_end, "owner": owner, "id": id};
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
    result_text = {"statusCode": 200, "status": "fail"}

    if width and height and location and owner:
        try:
            sql = 'INSERT INTO spots (width, height, owner, location, price, user_time_start, user_time_end) values ("{width}", "{height}", "{owner}", "{location}", "{price}", "{user_time_start}", "{user_time_end}");'.format(width=width, height=height, owner=owner, location=location, price=price, user_time_start=user_time_start, user_time_end=user_time_end);
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
    user_time_start = j_data['user_time_start'];
    user_time_end = j_data['user_time_end'];
    result_text = {"statusCode": 200, "status": "fail"}

    if id:
        try:
            sql = 'UPDATE spots SET width="{width}", height="{height}", location="{width}", price="{price}", user_time_start="{user_time_start}", user_time_end="{user_time_end}" where id={id};'.format(width=width, height=height, owner=owner, location=location, price=price, user_time_start=user_time_start, user_time_end=user_time_end, id=id);
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
   `width` INT NOT NULL,
   `height` INT NOT NULL,
   `owner` varchar(100) NOT NULL,
   `location` varchar(100) NOT NULL,
   `user_time_start` INT,
   `user_time_end` INT,
   `price` INT
    )
    '''
    cursor.execute(sql);

EnsureParkingSpotsTable();


 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()