import sqlite3


conn = sqlite3.connect('mydb.db')
cusror = conn.cursor()
# cusror.execute("CREATE TABLE if not exists apirelease( buildtime date, version varchar(30) primary key, links varchar2(30), methods varchar2(30))")
# conn.execute("Insert into apirelease values ('2020-10-5 8:49:00', 'v1','/api/v1/users','get, post, put, delete')")
# cusror.execute("CREATE TABLE if not exists users(username varchar2(30),full_name varchar2(30),email varchar2(30), password varchar(30),id integer primary key autoincrement)")

# #for key, user in enumerate(db_users):
# cusror.execute(
#         "Insert into users values ('alaa', 'Alaa Omar','alaa.omar2009@gmail.com','12345',1)")

api_list = []
cursor = conn.execute("SELECT * from users")
for row in cursor:
    user = {}
    user['username'] = row[0]
    user['name'] = row[1]
    user['email'] = row[2]
    user['password'] = row[3]
    user['id'] = row[4]
    api_list.append(user)


print(api_list)
conn.commit()
