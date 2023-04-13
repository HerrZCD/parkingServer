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
    print(data)
    print(j_data)
    print(j_data['name'])
    print(j_data['password'])

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
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()