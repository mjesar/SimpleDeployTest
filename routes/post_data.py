from flask import Blueprint,jsonify,request
import json
import pandas as pd

from databaseModel import db
from databaseModel import People
from databaseModel import  SameNames

post_api = Blueprint('post_api', __name__)

@post_api.route('/data/api/v1.0/input',methods=['POST','GET',])
def post_data():
    if request.method == 'POST':

            # request json for data force true for error in json farmate is wrong
            data = request.get_json(force=True)

            #save data to database from json post request
            people_db = People(first_name = data['first_name'],last_name = data['last_name'])
            #db.create_all()
            db.session.add(people_db)
            db.session.commit()

            #taking first_name and last_name from json post request
            first_name = data['first_name']
            last_name = data['last_name']

            # read and get length of complete rows
            dfObj = pd.read_csv("people.csv")
            len_index=len(dfObj['ID'])
            # print(len_index+1)

            dict = {}

            #append data to dictnary
            dict.update({"ID": [len_index+1], "First name": [first_name], "Last Name": [last_name]})

           #convert it to dataframe to can put to csv
            df = pd.DataFrame(dict)

            #open csv file flag "a" to append data and header which is columns would be only one time  bcs of header=f.tell() == 0
            with open("people.csv", 'a') as f:
                df.to_csv(f, mode='a', index=False, header=f.tell() == 0)


                #from df dataframe find duplicated values from only column first_name
                duplicateRowsDF = dfObj[dfObj.duplicated(['first_name'])]
                # print  duplicated values from only column first_name

                # convert dataframe to json object and returned it to api end point
                jsonfiles = json.loads(duplicateRowsDF["first_name"].to_json(orient='records'))

                #database work

                SameNames(same_name=jsonfiles)

                print(jsonfiles)
            return jsonify( {"Duplicated Names": jsonfiles})

    else:
            dfObj = pd.read_csv("people.csv")
            duplicateRowsDF = dfObj[dfObj.duplicated(['first_name'])]
            jsonfiles = json.loads(duplicateRowsDF["first_name"].to_json(orient='records'))
    return jsonify({"Duplicated Names" :jsonfiles})

