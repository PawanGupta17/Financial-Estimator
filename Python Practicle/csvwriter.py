import csv as cv
def profileinfo():
    dict={}

    csv_columns = ['uname','password','mobno']
    dict_data = []
    csv_file = "Names.csv"

    name=nameE.get()
    passw=pwordE.get()
    mobno=otpE.get()

    dict['uname']=name
    dict['password']=passw
    dict['mobno']=mobno

    dict_data.append(dict)
    print(dict_data)
    print(dict)
    try:
        with open(csv_file, 'a') as csvfile:
            writer = cv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
        print('rewev')
    except IOError:
        print("I/O error")

