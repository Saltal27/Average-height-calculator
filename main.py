# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

average_height = 0

for each_height in student_heights:
  average_height += each_height / (student_heights.index(student_heights[-1]) + 1)
print(round(average_height))


