from flask import Flask
from routes.post_data import post_api

# from databaseModel import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



app = Flask(__name__)


# configure SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aliali@localhost/people'

# initialized it with db object

db.init_app(app)

with app.app_context():
    # Imports

    # Initialize Global db
    db.create_all()



app.register_blueprint(post_api)



if __name__ == '__main__':
    app.run(debug=True)