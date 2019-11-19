def line_print(v_lines,delay):
    from time import sleep
    import sys

    for line in v_lines:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(delay)
        print('')


def choice_check(choice,lower,upper):
    if int_list.count(choice) == 0:
        print("Invalid input. Please enter {} to {}".format(lower,upper))
        return "bad"
    elif int(choice) >= lower and int(choice) <= upper:
        return "OK"
    else:
        print("Invalid input. Please enter {} to {}".format(lower,upper))
        return "bad"


def hiding(hide_place):
    if hide_place == "1":
        lines = [
                "",
                "You hear the bedroom door open. Through the closet door",
                "You can see the huge figure of the hockey masked figure towering in front of the doorway",
                "You see the long shining blade of a cruel machete he holds in his right hand"
                ""
                ]
    else:
        lines = [
                "",
                "You hear the bedroom door open. From under the bed",
                "You can see the huge figure of the hockey masked figure towering in front of the doorway",
                "You see the long shining blade of a cruel machete he holds in his right hand"
                ""
                ]


    line_print(lines,0.02)
    
    if hide_place == "1":
        if inv_list.count("Gun") == 0:       
            lines = [
                    "He suddenly rips the closet door of its hinges and lifts you out of the closet as if",
                    "you were a rag doll. The cold impassive face of the killer is the last thing you ever",
                    "see as he slides the cold blade of the machete through your heart."
                    ]

            line_print(lines,0.02)    
        else:
            lines = [
                    "He suddenly rips the closet door of its hinges. You level the gun at his chest and pull",
                    "the trigger. He Flinches and retreats back through the door. You now have no shotgun shells"
                    ]

            line_print(lines,0.02)
            
            inv_list.remove("Gun")
            inv_list.add("Empty Gun")
            
            bedroom()
    else:
        if inv_list.count("Gun") == 0:
            lines = [
                    "He suddenly flips the bed away from over your head as if he were lifting off just the",
                    "the bed covers. You have nowhere left to run to. The masked figure lifts you up to him and",
                    "he slides the cold blade of the machete through your heart."
                    ]

            line_print(lines,0.02)
        else:
            lines = [
                    "He suddenly flips the bed away from over your head as if he were lifting off just the",
                    "the bed covers. You raise the shotgun and empty the barrels into his chest. he Flinches and",
                    "leaves the room. you now have no shells for your shotgun"
                    ]

            line_print(lines,0.02)
            inv_list.remove("Gun")
            inv_list.append("Empty Gun")

            bedroom()



def attic():
    lines = [
            "",
            "You enter a dusty attic. The attic if full of old tea chests and suitcases.",
            "You see an arch window with cracked stained glass on the far wall",
            ""
            ]

    line_print(lines,0.02)
    
    finished = False
    c1 = False
    c2 = False

    while finished == False:
        choice = input("Do you 1) Search the boxes \n       2) Examine the Window \n    or 3) Return down the stairs")

        if choice_check(choice,1,3) == "OK":
            finished = True

        if choice == "1":
            if c1 and c2:
                lines = [
                        "you took too long exploring the attic. The huge figure enters the room, grabs you and throws you through the window",
                        "leaving you to fall to your death"
                        ]

                line_print(lines,0.02)
            else:
                lines = [
                        "You search amongst the boxes but find nothing to assist you",
                        "You hear someone smashing up the house downstairs"
                        ]

                line_print(lines, 0.02)

                c1 = True
                finished = False
        elif choice == "2":
            if c1 and c2:
                lines = [
                        "you took too long exploring the attic. The huge figure enters the room, grabs you and throws you through the window",
                        "leaving you to fall to your death"
                        ]

                line_print(lines, 0.02)
            else:
                lines = [
                        "you look through the window. You are far too high up to be able to jump out of and the wall is unscalable",
                        "You hear someone smashing up the house downstairs"
                        ]

                line_print(lines,0.02)
                        
                c2 = True
                finished = False
        elif choice == "3":
            if c1 and c2:
                lines = [
                        "you took too long exploring the attic. The huge figure enters the room, grabs you and throws you through the window",
                        "leaving you to fall to your death"
                        ]

                line_print(lines,0.02)
            else:
                upstairs()


def kitchen():
    lines = [
            "You enter what looks like a Victorian kitchen, with a very old oven, fireplace and table."
            ]

    line_print(lines,0.02)

    finished = False
    lever_found = False

    while finished == False:
        if lever_found == False:
            choice = input("Do you 1) Go through the door, \n       2) Search the table \n    or 3) Search the fireplace")

            if choice_check(choice,1,3) == "OK":
                finished = True

            if choice == "1":
                lines = ["You try to open the door but it won't shift"]

                line_print(lines,0.02)

                if inv_list.count("Axe") == 0:
                     finished = False
                else:
                    lines = ["You the swing the Axe at the doors hinges. After three tries the axe finally does its job and",
                             "The door falls over and you scramble into the night and escape",
                             ""]

                    line_print(lines,0.02)
                
            elif choice == "2":
                lines = ["You find nothing of use on the kitchen table"]
    
                line_print(lines,0.02)
                
                finished = False
            elif choice == "3":
                lines = ["You search the fireplace. Just under the mantlepiece you see a lever"]

                line_print(lines,0.02)
                lever_found = True
                finished = False
        else:
            choice = input("Do you 1) Go through the door, \n       2) Search the table \n    or 3) Pull the lever")

            if choice_check(choice,1,3) == "OK":
                finished = True

            if choice == "1":
                lines = ["You try to open the door but it won't shift"]

                line_print(lines,0.02)

                if inv_list.count("Axe") == 0:
                     finished = False
                else:
                    lines = ["You the swing the Axe at the doors hinges. After three tries the axe finally does its job and",
                             "The door falls over and you scramble into the night and escape",
                             ""]

                    line_print(lines,0.02)
                
            elif choice == "2":
                lines = ["You find nothing of use on the kitchen table"]
    
                line_print(lines,0.02)
                
                finished = False
            elif choice == "3":
                lines = ["You pull the lever. A secret door out of the house opens. You race through the door into the night air and escape"]

                line_print(lines,0.02)

                finished = True
                

def living_room():
    lines = ["",
             "You enter what looks like it was the house's living area. A mouldy couch lies in the centre of the room. ",
             "There are two crossed axes attached to the wall. There is also a door about 20 feet away on the right wall",
             ""
             ]

    line_print(lines,0.02)

    finished = False

    while finished == False:
        if inv_list.count("Axe") == 0:
            choice = input("Do you 1) Exit through the door to your right \n       2) Examine the Axes \n       3) Take the Left Axe \n    or 4) Take the Right Axe")

            if choice_check(choice,1,4) == "OK":
                finished = True

            if choice == "1":
                kitchen()            
            elif choice == "2":
                lines = [
                        "You notice a tripwire attached to the axe on the right"
                        ]

                line_print(lines,0.02)
            
                finished = False
            elif choice == "3":
                lines = ["You take the axe off the wall mount"]
                inv_list.append("Axe")
                finished = False

                line_print(lines,0.02)
                
            elif choice == "4":
                lines = [
                        "As you take the right axe off the wall you feel a tripwire attached to it activate a mechanism",
                        "Suddenly there is a wooshing which is the last thing you hear as a third axe rushes out of from the wall",
                        "and buries itself in your skull"
                        ]

                line_print(lines,0.02)
        else:
            choice = input("Do you 1) Exit through the door to your right \n       2) Examine the Right Axe \n    or 3) Take the Right Axe")

            if choice_check(choice,1,3) == "OK":
                finished = True

            if choice == "1":
                kitchen()            
            elif choice == "2":
                lines = [
                        "You notice a tripwire attached to the axe on the right"
                        ]

                line_print(lines,0.02)
            
                finished = False
            elif choice == "3":
                lines = [
                        "As you take the right axe off the wall you feel a tripwire attached to it activate a mechanism",
                        "Suddenly there is a wooshing which is the last thing you hear as a third axe rushes out of from the wall",
                        "and buries itself in your skull"
                        ]

                line_print(lines,0.02)


def basement(from_hall):

    if from_hall == False:
        lines = [
                "You fall down ten feet into a pitch black room",
                "You hear heavy breathing getting closer and closer"
                ]

        line_print(lines,0.02)

        finished = False
        
        while finished == False:
            choice = input("Do you 1) Search in the dark \n    or 2) Use the light on your phone to look around")

            if choice_check(choice,1,3) == "OK":
                finished = True

            if choice == "1":
                lines = [
                        "You start searching frantically for something to help you. Unforutnately your efforts are in vain.",
                        "You feel a pair of hands grab your throat and they start to squeeze the life out of you"
                        ]
                line_print(lines,0.02)
            elif choice == "2":
                lines = ["You switch on the torch of your phone. As you raise the beam you see the masked figure directly in front of you"]

                line_print(lines,0.02)
                
                if inv_list.count("Gun") == 0:
                    lines = ["You have no time to escape and the masked figure grabs you by the throat and squeezes the life out of you"]

                    line_print(lines,0.02)
                else:
                    lines = [
                            "You barely have time to shoot the figure in the chest with your gun. He winces and heads up the basement stairs",
                            "you find a light switch and switch it on."
                            ]

                    line_print(lines,0.02)
                    inv_list.remove("Gun")
                    basement(True)
    else:
        lines = [
                "",
                "You see an old basement with a single bulb illuminating the room.",
                "Debris is strewn around the room and you see a heavy door set at the back of the room",
                "You also see an old chest lying in the corner",
                ""
                ]

        line_print(lines,0.02)
        
        finished = False
        c1 = False
        c2 = False

        while finished == False:
            choice = input("Do you 1) Search the Debris \n       2) Open the Chest \n    or 3) Open the Door")

            if choice_check(choice,1,3) == "OK":
                finished = True

            if finished == True and c1 and c2:
                lines = ["Sadly you spent too long searching. The masked figure enters the room and in a single movement hurls his machete",
                         "right through your chest. You sink to the floor dead"]

                line_print(lines,0.02)
            elif choice == "1":
                lines = ["You search through the piles of wood and decaying boxes to no useful result"]

                line_print(lines,0.02)

                c1 = True
                finished = False
            elif choice == "2":
                lines = [
                        "You open the old chest, which turns out to be a large toolbox. Most of the contents have rotted beyond use,"
                        "but you do see a servicable crowbar, which you take."
                        ]

                line_print(lines,0.02)
                c2 = True
                inv_list.append("Crowbar")
                finished = False
            elif choice == "3":
                if inv_list.count("Crowbar") == 0:
                    lines = ["The door won't budge"]

                    line_print(lines,0.02)
                    
                    finished = False
                else:
                    lines = [
                            "You use the crowbar to pry open the door. On the other side of the door",
                            "you see a stone staircase leading up to the outside world. You bolt up the",
                            "stairs and race through the night air far away from danger"
                            ]

                    line_print(lines,0.02)
            
def secret_exit():
    lines = [
            "",
            "You examine the bookcase closely. You notice a book that looks out of place. You pull",
            "the book, and as you do so the whole bookcase rotates with you. Taking you into a dimly lit",
            "passage. You follow the passage for about 200 feet towards the light of day",
            "you emerge from the passage near to a roadside and frantically wave down a car",
            "",
            "Congratulations you have escaped"
            ]

    line_print(lines, 0.02)

def bedroom():
    if inv_list.count("Empty Gun") == 0:
        lines = [
                "",
                "You enter what appears to be the house's master bedroom.",
                "You see a classic four poster bed in the room, covered in cobwebs and complete",
                "with moth eaten bedding. You can hear loud footsteps coming up the stairs ",
                "outside the bedroom. Looking around the room you can see an old closet.",
                "You also see a bookcase",
                ""
                ]
    else:
        lines = [
                "",
                "You see a classic four poster bed in the room, covered in cobwebs and complete",
                "with moth eaten bedding. You can hear loud footsteps coming up the stairs ",
                "outside the bedroom. Looking around the room you can see an old closet.",
                "You also see a bookcase",
                ""
                ]

    line_print(lines,0.02)
    
    finished = False

    while finished == False:
        choice = input("Do you 1) Hide in the closet \n       2) Hide under the Bed, \n    or 3) Search the bookcase")

        if choice_check(choice,1,3) == "OK":
            finished = True

        if choice == "1" or choice == "2":
            hiding(choice)
        elif choice == "3":
            secret_exit()
    
def upstairs():
    lines = [
            "",
            "You walk up the decaying stairs which creak loudly underfoot",
            "When you reach the top of the stairs you see a claustrophobic hallway ahead",
            "of you. You can see a door to your left and a set of narrow stairs leading",
            "up to what you presume is the attic",
            "",
            "You hear a loud splintering crash from down below",
            "You will have to move fast"
            ]

    line_print(lines,0.02)

    finished = False

    while finished == False:
        choice = input("Do you 1) Go through the door, \n    or 2) Go up the attic stairs")

        if choice_check(choice,1,2) == "OK":
            finished = True

        if choice == "1":
            bedroom()
        elif choice == "2":
            attic()

def locked_room():
    lines = [
            "",
            "You unlock the door with the key and enter a study. A warped desk sits in front of the bay window. A moldy old yellow rug lies",
            "in the middle of the room.",
            "You see a shotgun sitting in a gun cabinet on the wall next to the door you entered through",
            "",
            "You hear a loud splintering crash from the entrance behind you",
            "You will have to move fast",
            ""
            ]
    

    line_print(lines, 0.02)

    finished = False
    rug_lifted = False
    study_visited = True
    
    while finished == False:
        if inv_list.count("Gun") == 0:
            if rug_lifted == False:  
                choice = input("Do You 1) Climb the ladder into the next room, \n       2) Examine Rug  \n    or 3) Take the Shotgun")

                if choice_check(choice,1,3) == "OK":
                    finished = True

                if choice == "1":
                    bedroom()

                if choice == "2":
                    lines = ["You lift the rug up and see a trapdoor beneath the rug"]

                    line_print(lines,0.02)
                    
                    rug_lifted = True
                    finished = False

                if choice == "3":
                    lines = ["You lift the shotgun out of the gun case and carry it with you"]
                    line_print(lines,0.02)
                    inv_list.append("Gun")
                    finished = False
            else:
                choice = input("Do You 1) Climb the ladder into the next room, \n    2) Enter the trapdoor \n    or 3) Take the shotgun")

                if choice_check(choice,1,3) == "OK":
                    finished = True

                if choice == "1":
                    bedroom()

                if choice == "2":
                    basement(False)

                if choice == "3":
                    inv_list.append("Gun")
                    finished = False                
        else:
            if rug_lifted == False:

                choice = input("Do You 1) Climb the ladder into the next room, \n    or 2) Examine the Rug")

                if choice_check(choice,1,2) == "OK":
                    finished = True

                if choice == "1":
                    bedroom()

                if choice == "2":
                    lines = ["You lift the rug up and see a trapdoor beneath the rug"]

                    line_print(lines,0.02)
                    rug_lifted = True
                    finished = False
            else:            
                choice = input("Do You 1) Climb the ladder into the next room \n    or 2) Enter the Trapdoor")

                if choice_check(choice,1,2) == "OK":
                    finished = True

                if choice == "1":
                    bedroom()
                if choice == "2":
                    basement(False)

    
def hallway():
    print("")

    lines = [
            "",
            "You see a gloomy hallway with peeling walls with old crumbling plaster lying on the floor.",
            "In the hallway there are two doors on each side of the hallway, and the hallway ends in a",
            "dark set of stairs leading into the basement",
            "",
            "You hear a loud splintering crash from behind you",
            "You will have to move fast",
            ""
            ]

    line_print(lines,0.02)

    finished = False

    while finished == False:
        choice = input("Do you 1) Go down to the basement, \n       2) Go through the Left door \n    or 3) Go to the Right door")

        if choice_check(choice,1,3) == "OK":
            finished = True

        if choice == "1":
            lines = [
                    "",
                    "You enter the pitch black stairway to the basement. You reach out to find a light switch to help you navigate the cold stone steps.",
                    "Luckily there is a light switch which you switch on"
                    ]

            line_print(lines,0.02)

            basement(True)
        elif choice == "2":
            living_room()
        elif choice == "3":
            kitchen()

    
def lobby():
    lines = [
        "",
        "You enter the abandoned mansion. The place has obviously not been lived in for decades. Black mold smears the old walls like an ugly tumorous growth.",
        "",
        "There are a set of dust covered stairs leading upwards. You see a closed carved wooden door to your right and ",
        "a hallway leading away to your left"
        ]

    line_print(lines,0.03)

    if inv_list.count("Key") == 0:
        
        lines = ["You see an old brass key lying on the rotting table standing in the middle of the room"]
        line_print(lines,0.03)

    print("")

    finished = False

    while finished == False:
        if inv_list.count("Key") == 0:
            choice = input("Do you 1) Go Upstairs, \n       2) Go through the door on the right, \n       3) Walk down the hallway \n    or 4) Pick up the Key ?")

            if choice == "4":
                lines = ["You pick up the key and put it in your pocket"]

                line_print(lines,0.03)
                inv_list.append("Key")
            else:
                if choice_check(choice,1,4) == "OK":
                    finished = True
        else: 
            choice = input("Do you 1) Go Upstairs, \n       2) Go through the door on the right, \n    or 3) Walk down the hallway")

            if choice_check(choice,1,3) == "OK":
                finished = True

        if choice == "2" and inv_list.count("Key") == 0:
            lines = ["The door seems to be locked"]

            line_print(lines,0.03)
            
            finished = False           
        elif choice == "1":
            upstairs()
        elif choice == "2":
            locked_room()
        elif choice == "3":
            hallway()

def plane_journey():
    skip_intro = input("Skip intro ? (y/n)")

    if skip_intro.lower() == "n":
        lines = [
            "Madrid. It's just another routine dull flight....right??",
            "You are about one hour into the flight when you look out of the window and see a man wearing a hockey mask hacking at the engine cover with a glistening machete. You question your sanity. "
            "You're about to ask the passenger next to you to check if they can see the same thing",
            "when the figure stops attacking the engine and slowly turns to you and points his blade right at you.",
            "You feel your blood freeze. You finally remember to ask the passenger next to you to look at the engine",
            "They look past you and say it looks fine. You turn to look back and see all is well. You must really need this break.",
            "",
            "You are about to close your eyes when you feel the plane lurch. You look back out of the window",
            "and the masked figure is now through the cover and hacking at the engine's workings. "
            "The plane suddenly drops and you feel your stomach rise",
            "into your throat. The plane plummets towards the earth. All the while the figure is manically slashing",
            "at the engine with his blade. The plane's remaining engines scream as they try to keep the plane airborne",
            "But it's no use. The planes keeps dropping closer and closer to the ground until",
            "the plane ploughs into the earth, the trees tear at the wings. Somehow you survive the smoke, the screams, the flames and scramble out of the twisted metal",
            "",
            "You see the trail of wreckage and debris all around you. About 100 metres away is an old house",
            "You are starting to regain your senses. The ringing in your ears is subsiding, when you see a huge piece of the plane's fuselage",
            "suddenly fly through the air right towards you. It barely misses you and crashes through the trees behind you",
            "You look to where the wreckage came from and see the figure wearing the hockey mask standing seven feet tall walking slowly",
            "and relentlessly towards you. Instinctively you flee towards and into the old house"
        ]
    
        line_print(lines,0.04)
    
    lobby()
    
int_list = ["0","1","2","3","4","5","6","7","8","9"]        

quitgame = False

while quitgame == False:
    print("")
    print("Welcome to He's Behind You")
    print("")

    choice = input("Do you wish to 1) visit friends abroad \n               2) Drive to your parents \n            or 3) go on scenic train journey")

    if choice == "1":
        inv_list = [
            "Wallet",
            "Phone"
            ]

        plane_journey()

    elif choice == "2":
        print("")   
    elif choice == "3":
        print("")
        
    print("")
    print("")
    tryagain = input("Do you wish to try again (y/n)")

    if tryagain.lower() == "n":
        quitgame = True
        
    
print("done")


