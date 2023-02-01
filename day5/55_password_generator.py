#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ''
hard_password = []


for n in range(nr_letters):
    rd_n = random.randint(0, len(letters)-1)
    easy_password += letters[rd_n]
    hard_password.append(letters[rd_n])

for n in range(nr_symbols):
    rd_n = random.randint(0, len(symbols)-1)
    easy_password += symbols[rd_n]
    hard_password.append(symbols[rd_n])
    
for n in range(nr_numbers):
    rd_n = random.randint(0, len(symbols)-1)
    easy_password += numbers[rd_n]
    hard_password.append(numbers[rd_n])

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# hard_pw = random.sample(hard_password, len(hard_password))
# print(''.join(hard_pw))

random.shuffle(hard_password)
last_hard_pw = ''
for hpw in hard_password:
    last_hard_pw += hpw
print(last_hard_pw)
