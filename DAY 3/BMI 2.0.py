# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI2 = weight /(height**2)
BMI = round(BMI2)

if BMI <= 18.5:
    print(f"Your BMI IS {BMI}, you are underweight")
elif 25>=BMI>18.5:
    print(f"Your BMI IS {BMI}, you have a normal weight")
elif  25<BMI<30:
    print(f"Your BMI IS {BMI}, you are slightly overweight")
elif 30<=BMI<35:
    print(f"Your BMI IS {BMI}, they are obese")
else:
    print(f"Your BMI IS {BMI}, they are clinically obese")
    
    