import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Uppercase Alphabets
uppercase_letters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]




# Common Symbols
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~',
    '§', '±', '°', '€', '£', '¥', '©', '®', '™', '¢', '∞', 'µ', '¶', '•', '¬']
print("welcome the pass generator")
ur_letters=int(input("enter the number of letters: "))
ur_symbols=int(input("enter the number of symbols:"))
ur_numbers=int(input("enter the number of numbers:"))
password_list=[]
for i in range(0,ur_letters):
    password_list.append(random.choice(uppercase_letters))
for i in range(0,ur_symbols):
    password_list.append(random.choice(symbols))
for i in range(0,ur_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password=password+i
print(password)

