password = "my password"

if len(password) < 8:
    print("password is too short")
else:
    print(password)

test = 15

if test % 3 == 0 or test % 5 ==0:
    print(str(test) + " is divisble by 3 or 5")
else:
    print(str(test) + " is not divisble by 3 or 5")

num = 18

if num % 3 == 0 and num % 5 == 0:
    print("fizz buzz")
elif num % 3 == 0:
    print("fixx")
elif num % 5 == 0:
    print("buzz")
else:
    print(num)
