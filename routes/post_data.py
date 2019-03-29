from flask import Blueprint,jsonify,request
import csv
import pandas as pd



post_api = Blueprint('post_api', __name__)

@post_api.route('/data/api/v1.0/input',methods=['POST'])
def post_data():

    # request json for data force true for error in json farmate is wrong
    data = request.get_json(force=True)


    #taking first_name and last_name from json post request
    first_name = data['first_name']
    last_name = data['last_name']

    # read and get length
    count_id = pd.read_csv("people.csv")
    len_index=len(count_id['ID'])
    print(len_index+1)

    dict = {}

    #append data to dictnary
    dict.update({"ID": [len_index+1], "First name": [first_name], "Last Name": [last_name]})

   #convert it to dataframe to can put to csv
    df = pd.DataFrame(dict)

    #open csv file flag "a" to append data and header which is columns would be only one time  bcs of header=f.tell() == 0
    with open("people.csv", 'a') as f:
        df.to_csv(f, mode='a', index=False, header=f.tell() == 0)


    return jsonify({'InputedData': data})