user1_name = input("Enter your name: ") #input form
user1_age = int(input("Enter your age: "))
user1_height = float(input("Enter your height in meters: "))# type conversion
print(type(user1_name))
print(type(user1_age))
print(type(user1_height)) #type casting

#Q2 under task1
user_input_data= int(input("Enter your age: "))
user_age_addup=100-user_input_data
print(f'You will turn 100 years old in {user_age_addup} years.')

#Task 2, debugging
item_name= input("Enter the item name: ")# this is valid input form to accept string input
item_price= float(input("Enter the item price($): "))# this is valid input form to accept float input
quantity = int(input("How many do you want to buy: "))# this is valid input form to accept integer input
subtotal = item_price*quantity
print(f'The subtotal for {quantity} {item_name}(s) is ${subtotal:.2f}')# this is valid output form to display the subtotal with 2 decimal places

#Task 3, Write a clean code.
distance_taken = float(input("Enter the distance taken in kilometers: "))# this is valid input form to accept float input
time_taken = float(input("Enter the time taken in hours: "))# this is valid input form to accept float input
calculate_distance = distance_taken / time_taken
print(f'The speed is {calculate_distance} km/h')# this is the valid output form to display the speed in km/

 

