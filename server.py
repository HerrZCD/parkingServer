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
def HandleRegister():
    data = request.get_data(as_text=True);
    j_data = json.loads(data);
    print(data)
    print(j_data)
    print(j_data['width'])
    print(j_data['height'])
    print(j_data['location'])
    print(j_data['price'])
    print(j_data['user_time_start'])
    print(j_data['user_time_end'])

    width = j_data['width'];
    height = j_data['height'];
    location = j_data['location'];
    price = j_data['price'];
    user_time_start = j_data['user_time_start'];
    user_time_end = j_data['user_time_end'];

    if width and height and location:
        try:
            sql = 'INSERT INTO spots (width, height, location, price, user_time_start, user_time_end) values ("{width}", "{height}", "{location}", "{price}", "{user_time_start}", "{user_time_end}");'.format(width=width, height=height, location=location, price=price, user_time_start=user_time_start, user_time_end=user_time_end);
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
   `id` INT UNSIGNED AUTO_INCREMENT,
   `width` INT NOT NULL,
   `height` INT NOT NULL,
   `location` varchar(100) NOT NULL,
   `user_time_start` INT,
   `user_time_end` INT,
   `price` INT,
    PRIMARY KEY ( `id` )
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