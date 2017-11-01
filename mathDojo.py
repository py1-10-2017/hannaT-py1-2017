# class MathDojo(object):
#     def __init__(self,num=0):
#         self.num =  num
#     def add(self, *num2):
#         self.num += sum(num2)
#         return self
#     def subtract(self, *num2):
#         self.num -= sum(num2)
#         return self
#     def result(self):
#         print self.num

# md = MathDojo().add(2).add(2,5).subtract(3,2).result()

class MathDojo(object):
    def __init__(self,*num):
        self.num =  num
        self.result = 0
    def add(self, *num2):
        for n in num2:
            if type(n) == list or type(n) == tuple:
                for i in n:
                    self.result += i
            else:
                self.result += n
        return self
    def subtract(self, *num2):
        for n in num2:
            if type(n) == list or type(n) == tuple:
                for i in n:
                    self.result -= i
            else:
                self.result +=n
        return self
    def result(self):
        print self.result

print MathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result