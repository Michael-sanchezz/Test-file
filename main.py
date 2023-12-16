import math

print("hello console")

my_name = "Michael Sanchez"
work_from_home = True
side = 15
radius = 10

print("\nMy name is " + my_name)
print("I work from home: " + str(work_from_home)) #casting - turning one data type into another
txt = "The length of each side of the square is {}"
print(txt.format(side))  #format string
print(f'The radius of the circle is {radius}')  #format literal string

square_area = side*side
square_perimeter = side*4
circle_area = math.pi * radius * radius
circle_perimeter = 2 * math.pi * radius
print("The square area is " + str(square_area) + " and the perimeter is " + str(square_perimeter))
print("The circle area is " + str(circle_area) + " and the perimeter is " + str(circle_perimeter))

print()
travel_options = ["foot", "bike", "car", "airplane"]
print("The travel options are:")
print(f"1) {travel_options[0]}")
print(f"2) {travel_options[1]}")
print(f"3) {travel_options[2]}")
print(f"4) {travel_options[3]}")

#y = 1
#for x in travel_options:
 #   print(f"{y}) {x}")
  #  y = y + 1

travel_type = input("How would you like to travel?\n ")
print("Travel type: " + travel_type)
distance = 100
time = 0
cost = 0
if travel_type == "foot":
    print("Walking is free! Speed is 3mph")
    cost = 0
    time = distance / 3
elif travel_type == "bike":
    rent_bike = input("Do you need to rent a bike? (yes or no) ")
    if rent_bike == "yes":
        print("Bike rental is $45! Speed is 10mph")
        cost = 45
        time = distance / 10
    else:
        print("Biking is free! Speed is 10mph")
        cost = 0
        time = distance / 10
elif travel_type == "car":
    print("Driving is $0.25/mi. Speed is 60mph")
    cost = 0.25 * distance
    time = distance / 60
elif travel_type == "airplane":
    print("Flying is $0.10/mi. Speed is 400mph")
    passenger_count = input("How many passengers? ")
    cost = .10 * distance * int(passenger_count)
    time = distance / 400
else:
    print(f"Sorry. {travel_type} is an invalid option")

print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")
cost_bar = "Cost: "
time_bar = "Time: "
for x in range(0,math.ceil(cost)):
   cost_bar += "$"
print(cost_bar)  # "Cost: $$$"
for y in range(0, math.ceil(time)):
    time_bar += "/"
print(time_bar)