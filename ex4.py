cars = 100 #define te variable type (int) and the quantity
space_in_a_car = 4 #define te variable type (int) and the quantity
drivers = 30 #define te variable type (int) and the quantity
passengers = 90 #define te variable type (int) and the quantity
cars_not_driven = cars - drivers #make operations with variables and add new variables
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.") #izpylnqvame po-gorni operacii i dobavqme tekst kym rezultatite
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")