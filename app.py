from flask import Flask, jsonify, make_response


from routes.post_data import post_api


app = Flask(__name__)




app.register_blueprint(post_api)



if __name__ == '__main__':
    app.run(debug=True)