class employee:
    def setnumberofworkingours(self):
        self.numberofworkingours=40

    def displaythenumberofworkinghours(self):
        print(self.numberofworkingours)

class Trainee(employee):
    def setnumberofworkingours(self):
        self.numberofworkingours=45

    def resetnumberofworkinghours(self):
        super().setnumberofworkingours()
emp=employee()
emp.setnumberofworkingours()
print("number of working hours of employees: ", end=" ")
emp.displaythenumberofworkinghours()

trainee=Trainee()
trainee.setnumberofworkingours()
print("Number of working hours for trainee: ", end= " ")
trainee.displaythenumberofworkinghours()
trainee.resetnumberofworkinghours()
print("number of working hours post reset:", end= " ")
trainee.displaythenumberofworkinghours()
