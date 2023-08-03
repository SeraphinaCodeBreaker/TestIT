class vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model  
    
class car(vehicle):
  def __init__(self, make, model, doors):
    super()._init_(make, model)
    self.doors = doors
    
class truck(vehicle):
  def __init__(self, make, model, bed_length):
    super()._init_(make, model)
    self.bed_length = bed_length
    
new_vehicle = input("Enter 1 to make a car, 2 to make a truck, or 3 to stop.")

if new_vehicle == "1":
  car_make = input("What is the make of your car? ")
  car_model = input("What is the model of your car? ")
  car_doors = input("How many doors does it have? ")
  print(f"You have a {car_make} {car_model} with {car_doors} doors.")
  
elif new_vehicle == "2":
  truck_make = input("What is the make of your truck? ")
  truck_model = input("What is the model of your truck? ")
  truck_bed = input("How long is your truck bed? ")
  print(f"You have a {truck_make} {truck_model} with {truck_bed} foot truck bed.")
  
elif new_vehicle == "3":
  raise SystemExit



