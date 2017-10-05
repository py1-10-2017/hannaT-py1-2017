#odd/even
def odd_even():
    for num in range (1,2000):
        if num %2 != 0:
            print "Number is {}".format(num) + ". This is an odd number."
        else:
            print "Number is {}".format(num) + ". This is an even number."
        
odd_even()

#multiply
a =  [2,4,10,16]
def multiply(arr,c):
    b = []
    for num in arr:
        b.append(num*c)
    print b
multiply(a,5)

# #Hacker Challange
def multiply(arr,c):
    b = []
    for num in arr:
        b.append(num*c)
    return b

def layered_multiples(arr):
    new_array = []
    for num in arr:
        inner_array = []
        for i in range(0,num):
            inner_array.append(1) 
        new_array.append(inner_array)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x