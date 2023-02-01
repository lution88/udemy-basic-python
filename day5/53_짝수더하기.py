#Adding Evens
total_number = 0
# 방법 1) 
for number in range(2, 101, 2):
    total_number += number
print(total_number)

# 방법 2)
total_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_number += number
print(total_number)