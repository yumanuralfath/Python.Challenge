# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height2=float(height)
weight2=float(weight)
result = weight2 /(height2**2)
hasil = int(result)
print("nilai BMI={} " .format(hasil))
if 18.5>hasil<24.9:
    print("Anda Normal")
else:
    if 25>hasil<29.9:
        print("Anda Normal")
    else:
        if hasil<18.5:
            print("Anda Kurang gizi")
        else:
            print("Anda Semok")


