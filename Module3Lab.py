# Brooke Perez
# Case Study: Lists, Functions, and Classes
# This program takes input for an automobile such as year, make, model, door number, and roof type. Once the program has all the information it will print.


class Vehicle:
    def __init__(self, type):
        valid_types = [
            "car",
            "truck",
            "plane",
            "boat",
            "broomstick"
        ]

        if type not in valid_types:
            raise (f"{type}, is not a valid vehicle type.")
        
        self.type = type


class Automobile(Vehicle):
    def __init__(self, year = None, make = None, model = None, doors = None, roof= None):
        super().__init__("car")
              
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def integer_validation(integer_input):
     if not integer_input.strip():
          raise ValueError("Input was not entered.")
     try:
          return int(integer_input)
     except ValueError:
        raise ValueError("Input needs to be a number.")
    
def string_validation(string_input):
     if not string_input.strip():
          raise ValueError("Input was not entered")
     return string_input
     
def main():
  
    user_car = Automobile()
    while True:
        try:
            user_car.year = integer_validation(input("Please enter the vehicles year: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            user_car.make = string_validation(input("Please enter the make: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            user_car.model = string_validation(input("Please enter the model: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            user_car.doors = integer_validation(input("Please enter the number of doors your vehicle has: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            user_car.roof = string_validation(input("Please enter the type of roof your vehicle has: "))
            break
        except ValueError as e:
            print(e)


    print(f"""
        Vehicle type: {user_car.type}
        Year: {user_car.year}
        Make: {user_car.make}
        Model: {user_car.model}
        Doors: {user_car.doors}
        Roof type: {user_car.roof}
    """)

main()