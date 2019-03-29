from flask import Blueprint,jsonify,request
import csv

post_api = Blueprint('post_api', __name__)

@post_api.route('/data/api/v1.0/input',methods=['POST'])
def post_data():

    data = request.get_json(force=True)

    id=data["id"]
    first_name = data["first_name"]
    last_name = data["last_name"]

    people_data = open('people.csv', 'w')

    csvwriter = csv.writer(people_data)

    count = 0

    for emp in data:

        if count == 0:
            header = emp

            csvwriter.writerow(header)

            count += 1

        csvwriter.writerow(emp)

    people_data.close()

    # csv_columns = ['No', 'Name', 'Country']
    # dict_data = [
    #     {'id': 1, 'Name': 'Alex', 'Country': 'India'},
    #     {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
    #     {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
    #     {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
    #     {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    # ]
    # csv_file = "Names.csv"
    # try:
    #     with open("people.csc", 'w') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #         writer.writeheader()
    #         for data in dict_data:
    #             writer.writerow(data)
    # except IOError:
    #     print("I/O error")


        # with open('people.csv', 'w') as csvfile:
    #     filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     filewriter.writerow(['ID', 'First Name', "Last Name"])
    #
    #     filewriter.writerow([id, first_name,last_name])

    return jsonify({'InputedData': data})