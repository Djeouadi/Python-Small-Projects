print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
Welcome to DEATH ISLAND 
There are two doors in front of you 🚪 a red door and 🚪 a blue door """)
door=str(input("Which door you want to open? "))
if door.lower()=="blue":
    print("""Oops,You chose the crocodile door.
    Game over 🐊🐊🐊""") 
elif door.lower()=="red":
    print("""Great ,Now you entered the room
              you found 3 boxes :📦 White ,📦 Black,📦 Green""")
    boxes=str(input("Which box you want to open ? "))
    if boxes.lower()=="white":
            print(" Oops,You opened a box filled with snakes 🐍🐍🐍")
    elif boxes.lower()=="black":
            print("Oops,You opened a box filled with spiders 🕷️🕷️🕷️ ")
    elif boxes.lower()=="green":
            print(" Congratulations , You found the treasure 💰💰💰")
    else:
     print("Invalid choise 🤷‍♂️🤷‍♂️🤷‍♂️")
else: 
   print("YOU chose invalid door please try again")