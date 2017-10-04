# words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
new_words= words.replace('day', 'month')
print new_words

# #min/max
x = [2,54,-2,7,12,98]
print "Minimum value of x is {}" .format(min(x))
print "Maximum value of x is {}" .format(max(x))

# #First/Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
y = [x[0], x[len(x)-1]]

#New List
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
a = x[:len(x)/2]
b = x[len(x)/2:]
b.insert(0,a)
print b