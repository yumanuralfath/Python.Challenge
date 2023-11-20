# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) # type: ignore
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
for height in student_heights:
    height2 = int(height)
    total_height += height2

BanyakData = 0
for JlData in student_heights:
    BanyakData += 1
print(BanyakData)

Rata2 = total_height / BanyakData
print(round(Rata2))