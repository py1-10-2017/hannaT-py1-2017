from datetime import datetime
class Call(object):
    uniq_id = 0
    def __init__(self, name, phone_number, reason):
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = datetime.now()
        self.reason = reason
        Call.uniq_id += 1 
    def display(self):
        print self.name
        print self.phone_number
        print self.time_of_call
        print self.reason
        print "id = {}".format(self.uniq_id)
call = Call('John','787-986-9876', 'help' )
call.display()
call2 = Call('Jane','787-936-9876', 'more help' )
call2.display()

class CallCenter(object):
    def __init__(self):
        self.calls = []
    def queue_size(self):
        return len(self.calls)
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self, call):
        self.calls.remove(self.calls[0])

call_center = CallCenter()
call_center.add(call).add(call2).remove(call)
print "queue size is {}".format(call_center.queue_size())