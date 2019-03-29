#Flask app to save the CSV file consists of three columns: ‘id’, ‘first_name, ‘last_name’.

using Python Flask Pandas

1:http://127.0.0.1:5000/data/api/v1.0/input
 route created to post data that save to csv file

To check this route in postman use this json pattern 
````json
{
	"first_name": "first name here",
	"last_name": "last name here"

}
````

Getting data From json post 
```python

    data = request.get_json(force=True)

    first_name = data['first_name']
    last_name = data['last_name']


```


Writing to cvs with the help of Pandas dataframe 

```python
 dict = {}
    dict.update({"First name": [first_name], "Last Name": [last_name]})
    df = pd.DataFrame(dict)
    with open("people.csv", 'a') as f:
        df.to_csv(f, mode='a', index=False, header=f.tell() == 0)
```


Autoincrement ID first check the length of index then increase it by one
```python
    # read and get length
    count_id = pd.read_csv("people.csv")
    len_index=len(count_id['ID'])
    
    #append data to dictnary
    #len_index+1 incrementing id
    dict.update({"ID": [len_index+1], "First name": [first_name], "Last Name": [last_name]})

```