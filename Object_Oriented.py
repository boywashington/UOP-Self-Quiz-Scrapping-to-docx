# class Microwave:
#     def __init__(self, brand: str, power_rating: str) -> None:
#         self.brand = brand
#         self.power = power_rating

# smeg: Microwave = Microwave(brand="Smeg", power_rating="B")
# print(smeg)
# print(smeg.brand)
# print(smeg.power)

# bosch: Microwave = Microwave(brand="Bosch", power_rating="A")
# print(bosch)
# print(bosch.brand)
# print(bosch.power)

class Staff:
    def __init__(self, name: str, shift: str):
        self.name = name
        self.shift = shift

    def start_work(self):
        print(f"{self.name} has started working on the {self.shift} shift.")    

class Waiter(Staff):
    def take_order(self):
        print(f"{self.name} is taking an order.")

    def serve_food(self):
        print(f"{self.name} is serving food.")

class Chef(Staff):
    def prepare_food(self):
        print(f"{self.name} is preparing food.")    
 
Raj = Waiter("Raj", "day") # this called object instantiation, and Raj is an object of the Waiter class
Simran = Waiter("Simran", "night") # this called object instantiation, and Simran is an object of the Waiter class
Amit = Chef("Amit", "day") # this called object instantiation, and Amit is an object of the Chef class

Raj.take_order()
Raj.start_work()

Amit.prepare_food()
Amit.start_work()   

Simran.serve_food()