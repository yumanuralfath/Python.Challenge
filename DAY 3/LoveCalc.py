# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_Ketek = name1.lower()
name_Ketek2 = name2.lower()
FullName = name_Ketek + name_Ketek2
T = FullName.count('t')
R = FullName.count('r')
U = FullName.count('u')
E = FullName.count('e')
angka_1 = T + R + U + E

L = FullName.count('l')
O = FullName.count('o')
V = FullName.count('v')
E = FullName.count('e')
angka_2 = L + O + V + E

Love_Calc = str(angka_1) + str(angka_2)
love_calc = int(Love_Calc)

if love_calc<10 or love_calc>90:
    print(f"Your score is {love_calc}, you go together like coke and mentos.")
elif 40 < love_calc < 50:
    print(f"Your score is {love_calc}, you are alright together.")
else:
    print(f"Your score is {love_calc}.")
