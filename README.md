# parkingServer

## 安装

首先要有mysql和python
```
 git clone https://github.com/HerrZCD/parkingServer.git
 cd parkingServer
 pip -r requirements.txt
```

本地打开mysql，登录 创建一个叫parking2的数据库
```
mysql -h localhost -u root -p
> (输入密码)

create database parking2

```

修改下server.py

```
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Amawenfei421',
                     database='parking2')

```

host user password 换成你数据库的host 用户名密码
python -m flask --app server run --debug
或者
python3 -m flask --app server run --debug
运行
