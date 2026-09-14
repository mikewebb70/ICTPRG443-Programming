print("What is the Weather today?")

weather =  input ("Rain (R), Hot(H)? ")

# if weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# print("Hope you have a lovely day")


# print("What is the Weather today?")

# weather =  input ("Rain (R), Hot(H)? ").upper()

# if weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# else:
#     print("Remmebr put your sunblock on")
#     print("Remember your Hat")
# print("Hope you have a lovely day")


# if weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# elif weather == "H":
#     print("Remmebr put your sunblock on")
#     print("Remember your Hat")
# else:
#     print("I did not understand your weather condition")
# print("Hope you have a lovely day")





# # Challenge 1 - combine slide to improve the weather app
# lecturer = input("Do you have a lecturer? ").upper()

# if lecturer == "Y":
#     if weather == "R":
#         print("Its fine you are in class anyway")
#     elif weather == "H":
#         print("Its sunny but you have a class")
#     else:
#         print("I did not understand your weather condition")
# else:
#     if weather == "R":
#         print("It is raining today")
#         print("Remember to take an umbrella")
#     elif weather == "H":
#         print("Remmebr put your sunblock on")
#         print("Remember your Hat")
#     else:
#         print("I did not understand your weather condition")

# print("Hope you have a lovely day")




# # Challenge Refactored
# if lecturer == "Y" and weather == "R":
#     print("Its fine you are in class anyway")
# elif lecturer == "Y" and weather == "H":
#     print("Its sunny but you have a class")
# elif lecturer != "Y" and weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# elif lecturer != "Y" and weather == "H":
#     print("Remember put your sunblock on")
#     print("Remember your Hat")
# else:
#     print("I did not understand your weather condition")






# # Challenge 2 - Add temperture for todays and see if is hotter or colder than the two days previous
#  # Challenge 2 start
# # Temperature for the previous two days
# temp_yesterday = 25  # example value
# temp_day_before = 26  # example value

# # Input for today's temperature
# try:
#     temp_today = int(input("Enter today's temperature: "))
# except:
#     print("Invalid input. Please enter a number.")

# # Check if today's temperature is hotter or colder than the previous two days
# if temp_today > temp_yesterday and temp_today > temp_day_before:
#     print("It's hotter today.")
# elif temp_today < temp_yesterday and temp_today < temp_day_before:
#     print("It's colder today.")
# else:
#     print("The temperature is similar to the previous days.")
# # Challenge 2 stop


# if lecturer == "Y" and weather == "R":
#     print("Its fine you are in class anyway")
# elif lecturer == "Y" and weather == "H":
#     print("Its sunny but you have a class")
# elif lecturer != "Y" and weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# elif lecturer != "Y" and weather == "H":
#     print("Remember put your sunblock on")
#     print("Remember your Hat")
# else:
#     print("I did not understand your weather condition")







# # Chellenge 3 - check the 2 days previous and store the highest and lowest temperature
# # Input for today's temperature
# try:
#     temp_today = int(input("Enter today's temperature: "))
# except:
#     print("Invalid input. Please enter a number.")

# ## Challenge 4 start
# # Initialize max_temp and min_temp
# max_temp = temp_yesterday
# min_temp = temp_yesterday

# # Check if temp_day_before is the new max or min
# if temp_day_before > max_temp:
#     max_temp = temp_day_before
# elif temp_day_before < min_temp:
#     min_temp = temp_day_before

# # Check if temp_today is the new max or min
# if temp_today > max_temp:
#     max_temp = temp_today
# elif temp_today < min_temp:
#     min_temp = temp_today
# # Challeneg 4 stop

# # Check if today's temperature is hotter or colder than the previous two days
# if temp_today > temp_yesterday and temp_today > temp_day_before:
#     print("It's hotter today.")
# elif temp_today < temp_yesterday and temp_today < temp_day_before:
#     print("It's colder today.")
# else:
#     print("The temperature is similar to the previous days.")


# if lecturer == "Y" and weather == "R":
#     print("Its fine you are in class anyway")
# elif lecturer == "Y" and weather == "H":
#     print("Its sunny but you have a class")
# elif lecturer != "Y" and weather == "R":
#     print("It is raining today")
#     print("Remember to take an umbrella")
# elif lecturer != "Y" and weather == "H":
#     print("Remember put your sunblock on")
#     print("Remember your Hat")
# else:
#     print("I did not understand your weather condition")


# if number < 2:
#     print('Below 2')
# elif number < 20:
#     print('Below 20')
# elif number < 10: 
#     print('Below 10')
# else:
#     print('Something else')

# if number < 2:
#     print('Below 2')
# elif number >= 2: 
#     print('Two or more')
# else:
#     print('Something else')

