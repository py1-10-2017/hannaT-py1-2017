import random
def coin_toss():
    
    head = 0
    tail = 0

    for num in range (1,5):
        toss = random.randint(0,1)
        print toss
        if toss == 0:
            head += 1
            print "Attempt #{}".format(num) + ": Throwing a coin....it's a head!....Got {}".format(head) +" head(s)so far and {}".format(tail)+" tail(s) so far"
        else:
            tail += 1
            print "Attempt #{}".format(num) + ": Throwing a coin....it's a tail!....Got {}".format(head) +" head(s)so far and {}".format(tail)+" tail(s) so far"
coin_toss()   