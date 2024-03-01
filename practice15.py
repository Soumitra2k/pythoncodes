class mathOperations:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

math_ops=mathOperations()

result1=math_ops.add(2,3,4)
print("result1:",result1)    # output = 9


# result2=math_ops.add(2,3)
# print("result2:", result2)  ## TypeError: mathOperations.add() missing 1 required positional argument: 'c'

