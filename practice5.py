import time

favfruits= ["apple","mango","berry","orange"]

print(favfruits)
for demo in favfruits:
    print(demo)

## range()
for number in range(1,10):
    print(number)   # it will print from 1 to 9


temp=77
while temp >=68 and temp <=77 :
    print("room temperature is maitained at {} deg F".format(temp))
    temp = temp-10
    #time.sleep(30)

    #while True:
        #print("This loop runs for ever")

#MATRIX 3 X 3

number=1
for row in range(1,4):
    for column in range(1,4):
        print(number,end=' ')
        number=number=number+1
    print()

print("new")
# Break

for number in range(1,11):
    if number== 15:
        break
    else:
        print(number)


# continue
print("new1")

for number in range(1,11):
    if number== 5:
        continue
    else:
        print(number)


# continue
print("new2")

for number in range(1,11):
    if number== 5:
        continue
    else:
        print(number)
else:
    print("all the numbers were printed without breaking")