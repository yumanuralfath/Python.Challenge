# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# diction = list(names)
banyak_Nama = len(names)

Choose_Name = random.randint(0, banyak_Nama-1)
namanya = names[Choose_Name]

if Choose_Name == 0:
        print(f"{namanya[0]} is going to buy the meal today!")
else:
        print(f"{namanya} is going to buy the meal today!")
        
        
        #code bagus
#         import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇

# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")
