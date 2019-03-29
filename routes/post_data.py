from flask import Blueprint,jsonify,request
import csv
import pandas as pd



post_api = Blueprint('post_api', __name__)

@post_api.route('/data/api/v1.0/input',methods=['POST'])
def post_data():

    data = request.get_json(force=True)



    first_name = data['first_name']
    last_name = data['last_name']

    dict = {}
    dict.update({"First name": [first_name], "Last Name": [last_name]})
    df = pd.DataFrame(dict)
    with open("people.csv", 'a') as f:
        df.to_csv(f, mode='a', index=False, header=f.tell() == 0)


    return jsonify({'InputedData': data})