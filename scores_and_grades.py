import random
def grades():
    random_num = random.randint(60,100)
    if random_num <= 69:
        print "Score {}".format(random_num) + "; Your grade is D"
    elif random_num <= 79:
        print "Score {}".format(random_num) + "; Your grade is C"
    elif random_num <= 89:
        print "Score {}".format(random_num) + "; Your grade is B"
    else:
        print "Score {}".format(random_num) + "; Your grade is A"
grades()    
