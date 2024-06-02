

# basic object oriented 

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} {self.model}"



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size



my_tesla=ElectricCar("tesla","model s","85kwh")

print(my_tesla.model)

# my_car=Car("Toyota","corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car=Car("tata","safari")

# print(my_new_car.model)
# print(my_new_car.full_name())




