from flask import Flask
from flask import jsonify
import json
import sqlite3
from flask import make_response

app = Flask(__name__)

@app.route('/api/v1/info')
def home_index():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list = []
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")
    for row in cursor:
        a_dict = {}
        a_dict['version'] = row[0]
        a_dict['buildtime'] = row[1]
        a_dict['methods'] = row[2]
        a_dict['links'] = row[3]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'api_version':api_list}),200


@app.route('/api/v1/users')
def get_users():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list = []
    cursor = conn.execute("SELECT * from users")
    for row in cursor:
        user = {}
        user['username'] =row[0]
        user['name'] = row[1]
        user['email'] = row[2]
        user['password'] = row[3]
        user['id'] = row[4]
        api_list.append(user)
    conn.close()
    return jsonify({'user_list': api_list}), 200


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def list_users(user_id):
    return list_users(user_id)


def list_users(user_id):
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list = []
    cursor = conn.execute(f"SELECT * from users where id=?", (user_id,))
    data = cursor.fetchall()
    if len(data) != 0:
        user = {}
        user['username'] = data[0][0]
        user['name'] = data[0][1]
        user['email'] = data[0][2]
        user['password'] = data[0][3]
        user['id'] = data[0][4]
        api_list.append(user)
    conn.close()
    return jsonify({'user_list': api_list})


@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({'error': 'Resource not found!'}), 404)


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400)
        user = {
            'username': request.json['username'],
            'email': request.json['email'],
            'name': request.json.get('name', ""),
            'password': request.json['password']
        }
    return jsonify({'status': add_user(user)}), 201


@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def add_user(new_user):
    conn = sqlite3.connect('mydb.db')
    print ("Opened database successfully");
    api_list=[]
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? or emailid=?",(new_user['username'],new_user['email']))
    data = cursor.fetchall()
    if len(data) != 0:
        abort(409)
    else:
        cursor.execute("insert into users (username, emailid, password,full_name) values(?,?,?,?)", (new_user['username'], new_user['email'], new_user['password'], new_user['name']))
        cursor.commit()
        return "Success"
    conn.close()
    return jsonify({api_list})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
