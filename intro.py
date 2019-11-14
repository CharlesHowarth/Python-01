
reakfast = my_name = "Charles"
my_age = 54
my_colour = "Purple"
"""
print("Name = " + my_name)
print("Age = " + str(my_age))
print("Food = " + my_food)

print("My name is {} and I am {} years old and my favourite colour is {}".format(my_name,my_age,my_colour))
print("")


breakfast = "toast"
lunch = "sandwuches"
dinner = "pizza"

print("Today's breakfast is {} and lunch is {} and dinner is {}".format(breakfast,lunch,dinner))

breakfast = "cereal"
lunch = "chips"
dinner = "curry"

print("Tomorrow's breakfast is {} and lunch is {} and dinner is {}".format(breakfast,lunch,dinner))

from datetime import date
today_date = date(2019, 11, 12)
my_birthday = date(2020, 10, 12)

day_count = my_birthday - today_date

print(day_count.days)

"""

space_1 = "X"
space_2 = "X"
space_3 = "O"
space_4 = "X"
space_5 = "X"
space_6 = " "
space_7 = "O"
space_8 = " "
space_9 = " "


print("   |   |   ")
print(" {} | {} | {} ".format(space_1, space_2 , space_3 ))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space_4, space_5 , space_6 ))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space_7, space_8 , space_9 ))
print("   |   |   ")


if space_1 == space_2 == space_3 and space_1 != " ":
    print("win on row 1")
else:
    print("no win on row 1")

print("")
print("")

