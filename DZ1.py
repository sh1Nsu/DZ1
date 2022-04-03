my_age = 18
print(f"Hello, I am {my_age} years old")
name = "Bogdan"
print(f'{5*(name)}')
while True:
    user_name = input("what's ur name? ")
    if user_name.isdigit():
        print("Write ur name correct!")
    else:
        break
while True:
    user_age = int(input("what's ur age? "))
    if user_age > 150 or user_age < 0:
        print("Error! You are using invalid symbols")
        user_age = int(input())
    else:
        break
print(f"Hello, {user_name}!")
print(f"U r {user_age} years old")
print(user_name[1:-1], user_name[::-1], user_name[-3:], user_name[0:5])
print(len(user_name))
summ = 0
composition = 1
while user_age > 0:
    summ += user_age % 10
    composition *= user_age % 10
    user_age //= 10
print(f"The sum of numbers in ur age = {summ}")
print(f"The comp = {composition}")
user_name2 = user_name.capitalize()
print(user_name.upper(), user_name.lower(), user_name.capitalize(), user_name2.swapcase())
print("what 2+2*2 is?")
while True:
    answer = int(input())
    if answer != 6:
        print("Try again!")
    else:
        print("correct!")
        break
