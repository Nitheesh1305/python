# This code will be executed if you `python carspackage` from terminal
from cars import Car
from suv import SUV

print("Let's create a Toyota RAV4!")
car = Car(make="Toyota", model="RAV4")
print(car)

print("\n---------------------------\n\n")

sport = SUV(make="MG", model="RAV4")
print(sport)

## UNCOMMENT BELOW PART WHEN NEEDED =================

# print("Let's receive arguments using sys.argv.")

# # Pass arguments
# import sys

# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)
 
# # Arguments passed
# print("Name of Python script:", sys.argv[0])
 
# print("\nArguments passed:",)
# for i in range(1, n):
#     print(sys.argv[i], "Type:", type(sys.argv[i]))
     
# print("\n\nLet's create a car, as per your suggestion!")        
# car = Car(make=sys.argv[1], model=sys.argv[2])
# print(car)