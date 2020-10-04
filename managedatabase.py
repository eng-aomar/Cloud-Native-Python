import sqlite3


conn = sqlite3.connect('mydb.db')
cusror = conn.cursor()
cusror.execute("CREATE TABLE if not exists apirelease( buildtime date, version varchar(30) primary key, links varchar2(30), methods varchar2(30))")
# conn.execute("Insert into apirelease values ('2017-01-01 10:00:00', 'v1','/api/v1/users','get, post, put, delete')")
cusror.execute("CREATE TABLE if not exists users(username varchar2(30),emailid varchar2(30),password varchar2(30), full_name varchar(30),id integer primary key autoincrement)")

db_users = ['alaa', 'ahmad', 'aysar', 'mila', 'lujain']

#for key, user in enumerate(db_users):
cusror.execute(
        "Insert into users values ('alaa', 'alaa.omar2009@gmail.com','12345','Alaa Omar',1)")
conn.commit()
