from flask import Flask, jsonify, make_response

from databaseModel import db

from routes.post_data import post_api


app = Flask(__name__)


# configure SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aliali@localhost/people'

# initialized it with db object
db.init_app(app)


app.register_blueprint(post_api)



if __name__ == '__main__':
    app.run(debug=True)