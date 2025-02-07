from flask import Flask
from models.product import db
from controllers.product_controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.17.0.2:3306/swarch2024ii_db'
db.init_app(app)

app.register_blueprint(product_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
