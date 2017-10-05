#part I
def names():
    students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    for student in students:
        print student["first_name"] + " " + student["last_name"]

names()

#part II

def users():
    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }
    print "Students"
    for i in range (len(users['Students'])):
        u = users['Students'][i]
        s = u["first_name"] + " " + u["last_name"]
        print "{}".format(i+1) + " - " + s + " - {}".format(len(s)-1)
    print "Instructors"
    for i in range (len(users['Instructors'])):
        u_i = users['Instructors'][i]
        ins = u_i["first_name"] + " " + u_i["last_name"]
        print "{}".format(i+1) + " - " + ins + " - {}".format(len(ins)-1)
users()