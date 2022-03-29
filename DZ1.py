bogdan = "hello"
myage = 18
print("Hello, I am ", myage, "years old")
name = "bogdan"
print(name + name + name + name + name, name*5)
while True:
    username = input("what's ur name? ")
    if username.isdigit():
        print("Write ur name correct!")
    else:
        break
while True:
    userage = int(input("what's ur age? "))
    if userage > 150 or userage < 0:
        print("Error!")
        userage = int(input())
    else:
        break
print("Hello,", username, "!")
print("U r", userage, "years old")
print(username[1:-1], username[::-1], username[-3:], username[0:5])
print(len(username))
s = 0
p = 1
while (userage > 0):
    s += userage%10
    p *= userage%10
    userage //= 10
print("The sum of numbers in ur age =", s)
print("The comp =", p )
username2 = username.capitalize()
print(username.upper(), username.lower(), username.capitalize(), username2.swapcase())
print("what 2+2*2 is?")
while True:
    answer = int(input())
    if answer != 6:
        print("Try again!")
    else:
        print("correct!")
        break
