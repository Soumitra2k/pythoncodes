number=1
for row in range(1,4):
    for column in range(1,4):
        print(number,end=' ')
        number=number+1
    print()

try:
    length=10
    width=0
    length/width
except NameError:
    print("variable has to be used before defining it")  # it will give this output and stop when variable is not defined and stop here
except ZeroDivisionError:
    print("division by 0 is invalid, change your input") # this will give this o/p when u are trying to devide by 0 and stop
except Exception:
    print("got a new error")   # when above exception is not there

finally:
    print("Finally block will be executed irrespetive of exception")



