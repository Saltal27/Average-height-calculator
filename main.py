# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Method 1
average_height = 0

for each_height in student_heights:
	average_height += each_height / (
	    student_heights.index(student_heights[-1]) + 1)
print(round(average_height))

# Method 2
# total_heights = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_heights / number_of_students)
# print(average_height)

# Method 3
# total_heights = 0
# for each_height in student_heights:
#   total_heights += each_height

# number_of_students = 0
# for each_student in student_heights:
#   number_of_students += 1

# average_height = round(total_heights / number_of_students)
# print(average_height)
