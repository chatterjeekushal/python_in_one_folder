

# basic object oriented 

class Car:
    
    total_car=0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
    
    
    def get_brand(self):
        return self.__brand
    
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "cars are menes of transpot"
    
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    
    def fuel_type(self):
        return "Electric charge"




my_tesla=ElectricCar("tesla","model s","85kwh")

# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())
# print(ElectricCar.general_description())

# print(my_tesla.full_name())

# print(isinstance(my_tesla,Car))





safari=Car("tata","safari")


# print(safari.general_description())

# print(Car.total_car)

# safari.model="nano"

# print(safari.model)








class Battery:
    def battery_info(self):
        return "this is  battery"


class Engine:
    def Engine_info(self):
        return "this is engine"


class  ElectricCartwo(Battery,Engine,Car):
    pass



my_bike=ElectricCartwo("royal emfid","h650")

print(my_bike.battery_info())
print(my_bike.Engine_info())
print(my_bike.get_brand())


