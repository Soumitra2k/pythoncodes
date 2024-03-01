cameras={"Sony":600,"nikon":500,"Canon":650}
print(cameras)
cameras["nikon"]=800
print(cameras)
print("Hi")
print(cameras.keys())
print(cameras.values())
copy_cameras=cameras.copy()
print("Hii")
print(copy_cameras)
del cameras["Sony"]
print(cameras)
cameras.clear()
print("Hello")
print(cameras)

#conditional statements
#----------------
#if condition
totalmarks=60

if totalmarks >= 90:
    print("you have cleared the exam with A grade")
elif totalmarks >= 40:
    print("congrats you have passed the exam")
else:
    print("you failed the exam")

totalmarks=92
if totalmarks >=90:
    print("congrats you have secured A grade")
    if totalmarks ==100:
        print("you got full marks")

#####

totalmarks-95
attendance=90

if totalmarks >=90 and attendance >=90:
    print("you are a very disciplined student")

#
fruit="apple"
if fruit is "mango" or fruit is "apple":
    print("i like that fruit")


