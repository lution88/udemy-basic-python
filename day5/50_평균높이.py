# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
student_count = 0
total_heights = 0
for n in range(0, len(student_heights)):
  student_count += 1
  student_heights[n] = int(student_heights[n])
  total_heights += student_heights[n]
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(round(total_heights / student_count))