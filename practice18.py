class car:

    def __init__(self,make,model,year):
        self.__make=make # this is a private attribute
        self.__model = model  # this is a private attribute
        self.__year = year  # this is a private attribute
        self.__is_started=False

    def start_engine(self):
        self.__is_started=True
        print("engine started")

    def stop_engine(self):
        self.__is_started = False
        print("engine stopped")

    def get_make(self):
        return self.__make


    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def is_engine_started(self):
        return self.__is_started

my_car=car("Toyota","Camry",2020)
print("Make:",my_car.get_make())
print("Model:",my_car.get_model())
print("Model:",my_car.get_year())


#print("make:",my_car.__make)

my_car.start_engine()
print("Engine Started:", my_car.is_engine_started())

my_car.stop_engine()
print("Engine Stopped:", my_car.is_engine_started())