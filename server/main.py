from flask import Flask, request, send_file
import json
import uuid
import os
from flaskext.mysql import MySQL
mysql = MySQL(autocommit=True)
app = Flask(__name__)  

app.config['MYSQL_DATABASE_USER'] = 'gamma'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'cars'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    

mysql.init_app(app)

cursror = mysql.connect().cursor()

# создание пользователя
@app.route('/create_user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    full_name_user = data['full_name_user']
    password = data['password']
    cursror.execute("INSERT INTO user_data (full_name_user, password) VALUES ('{}', '{}') ".format(full_name_user, password))
    return 'ok'

@app.route('/get_all_users', methods=['GET'])
def get_all():
    cursror.execute("SELECT * FROM user_data")
    data = cursror.fetchall()
    return json.dumps(data)

@app.route('/get_user', methods=['GET'])
def get_user():
    id = request.args.get('id')
    cursror.execute("SELECT * FROM user_data WHERE id = '{}'".format(id))
    data = cursror.fetchall()
    return json.dumps(data)

# создание автомобиля
@app.route('/create_car', methods=['POST'])
def create_car():
    data = json.loads(request.data)
    brand_of_cars = data['brand_of_cars']
    machine_model = data['machine_model']
    nambers_VIN = data['nambers_VIN']
    cursror.execute("INSERT INTO name_of_cars (brand_of_cars, machine_model, nambers_VIN) VALUES ('{}', '{}', '{}') ".format(brand_of_cars, machine_model, nambers_VIN))
    return 'ok'

@app.route('/get_all_cars', methods=['GET'])
def get_all_cars():
    cursror.execute("SELECT * FROM name_of_cars;")
    data = cursror.fetchall()
    return json.dumps(data)

@app.route('/get_car', methods=['GET'])
def get_car():
    id = request.args.get('id')
    cursror.execute("SELECT * FROM name_of_cars WHERE id = '{}'".format(id))
    data = cursror.fetchall()
    return json.dumps(data)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        print(request.files)
        print(request.form)
        if(not request.files['file']):
            return "ty debil"
        file = request.files['file']
        filename = file.filename
        name = str(uuid.uuid4())
        extension = filename.split('.')[1]
        name +='.'+extension
        if(file):
            file.save(os.path.join("server/uploads/", name))
            return name
    if request.method =='GET':
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''

@app.route('/get_file', methods=['GET'])
def get_file():
    filename = request.args.get('filename')
    return send_file('uploads/'+filename)
    







# @app.route('/')
# def index():
#     cursror.execute("SHOW DATABASES")
#     data = cursror.fetchall()
#     return json.dumps(data)

# @app.route('/add', methods=['POST'])
# def get_data():
#     data = request.get_json()
#     cursror.execute("INSERT INTO cars (name, price) VALUES (%s, %s)", (data['name'], data['price']))
#     return 'OK'

# @app.route('/name_of_cars', methods=['GET'])
# def get_name_of_cars():  
#     data = request.get_json() 
#     cursror.execute("INSERT INTO name_of_cars ( brand_of_cars, machine_model, numbers, nambers_VIN, car_charging_speed, engine_power, charging_type) VALUES ( '{brand_of_cars}', '{machine_model}, '{numbers}, '{nambers_VIN}, '{car_charging_speed}, '{engine_power}, '{charging_type}')".format(**data))
#     name_of_cars = cursror.fetchall()
#     return json.dumps(name_of_cars)

# @app.route('/create_charging_point', methods=['POST'])
# def create_charging_point():
#     data = request.get_json()
#     cursror.execute("INSERT INTO charging_points ( adress, coordinates) VALUES ( '{address}', '{coordinates}')".format(**data))
#     create_charging_point = cursror.fetchall()
#     return json.dumps({'status': 'ok'})

# # get charging point by id

# запусти приложение на локальном сервере
if __name__ == '__main__':
    app.run(debug=True, port=8080)