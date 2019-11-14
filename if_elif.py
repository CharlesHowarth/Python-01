time = 12
place_of_work = "Trafford College"
town_of_home = "Alty"

if time < 8 or time > 18:
    print("I'm at home")
elif time == 8 or time == 17:
    print("I'm commuting")
else:
    print("I'm at " + place_of_work)

print("")
