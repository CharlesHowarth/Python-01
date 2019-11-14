films = [
    "Alien",
    "Wicker Man",
    "Ghostbusters",
    "Goodfellas",
    "Silence of the Lambs"
    ]

films.append("The Haunting")
films.insert(4,"The Thing")

def film_check():
    if films[2] == "Ghostbusters":
        print("You'd better be talking the 1984 'busters")
    else:
        print("Ghosted")

for i in films:
    print(i)

film_check()
