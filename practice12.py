from practice11 import calculator
class childimpl(calculator) :
    num2=200
    def __init__(self) :
        calculator.__init__(self,2,10)
    def completedata(self) :
        return self.num2+self.num + self.summation()

obj= childimpl()
print(obj.completedata())