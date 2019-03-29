from flask import Blueprint,jsonify,request


post_api = Blueprint('post_api', __name__)

@post_api.route('/data/api/v1.0/input',methods=['POST'])
def post_data():

    data = request.get_json()



    return jsonify({'InputedData': data})