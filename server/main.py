from flask import Flask
import json
from flaskext.mysql import MySQL
mysql = MySQL(autocommit=True)
app = Flask(__name__)
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'gamma'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'cars'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

cursror = mysql.connect().cursor()

@app.route('/')
def index():
    cursror.execute("SHOW DATABASES;")
    return json.dumps(cursror.fetchall())
    

# запусти приложение на локальном сервере
if __name__ == '__main__':
    app.run(debug=True)