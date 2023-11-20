# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n]) # type: ignore
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maxxx = 0
for maks in student_scores:
    if maks > maxxx : # type: ignore
        maxxx = maks
print(f"The highest score in the class is: {maxxx}")