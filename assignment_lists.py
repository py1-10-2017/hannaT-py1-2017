l = [2,3,1,7,4,12]
string = "String:"
sum = 0
str_type = False 
int_type = False
float_type = False
for item in l:
    if type(item) is str:
        string = string + " "+ item + " "
        str_type = True
    elif type(item) is float or int:
        sum += item
        if type(item) is float:
            float_type = True
        else:
            int_type = True
if int_type and float_type and str_type:
    print "The list you entered is of mixed type"
    print string
    print "Sum: {}".format(sum)
elif int_type:
    print "The list you entered is of integer type"
    print "Sum: {}".format(sum)   
elif float_type:
    print "The list you entered is of float type"
    print "Sum: {}".format(sum)
elif str_type:
    print "The list you entered is of string type"
    print string
