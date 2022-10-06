import random

start = input("Would you like to play? If so type (start): ")
if start != "start":
    print("Come on man I worked hard on this!")
if start == "start":
    print("Now that's what I'm talking about.")
    
    dice = random.randint (1, 25)
    hp = 100
    atk = 10
    defense = 10
    speed = 10
    monster = random.randint (1, 100)
    weapon = random.randint (1, 5)
    level = 1
    
    choice1 = input("You encounter a sword! Do you pick it up? (yes) or (no): ")
    if choice1 == "yes":
        print("You picked up the sword!")
        print("The sword has a rarity of:", int(2))
        atk += 2
    if choice1 == "no":
        print("You left the sword to rot on the ground.")
        print("Yeah I would have done the same!")
        
    print("Current stats: " "Hp", int(hp), "Def", int(defense), "Atk", int(atk), "Spd", int(speed), "Lv", int(level))
    choice2 = input("You walk into a forest and encounter a monster...do you attack it? (yes) or (no)")
    if choice2 == "yes":
        print("Monster Power:", int(3))
        print("Your Atk:", int(atk))
        print("Monster attacks you doing", int(4), "damage.")
        print("You attack the monster doing", int(atk), "damage.")
        print("The monster fled!")
        level+= 1
        hp -= 4
        
    if choice2 == "no":
        print("The monster attacked you then fled!")
        print("You take", int(4), "damage")
        hp -= 4
        
    print("Current stats: " "Hp", int(hp), "Def", int(defense), "Atk", int(atk), "Spd", int(speed), "Lv", int(level))
    choice3 = input("After that little incident you seemed to be hurt, luckly you came across a sachet that smells like delicious food! Do you take it? (yes) or (no)")
    if choice3 == "yes":
        print("You take the food and eat it recovering", int(2), "Hp.")
        print("But you gain a poison effect for the next 3 scenes")
        hp += 2 - 1
        
    if choice3 == "no":
        print("You don't touch the sachet and continue to walk too your next destination!")
        print("heres 3 extra ponts of hp")
        hp += 3
        
    print("Current stats: " "Hp", int(hp), "Def", int(defense), "Atk", int(atk), "Spd", int(speed), "Lv", int(level))
    choice4 = input("You come to a cross road, there are 3 paths, which one do you go down? 1, 2 or 3?: ")
    if choice4 == "1":
        print("You go down the first path.")
        print("Welcome to easy mode, in this mode all of your stats are now 150")
        print("Password for Easy.py:", int(799905))
        hp = 150
        defense = 150
        atk = 150
        speed = 150
        print("Go to github and download the easy.py file.")
        
    if choice4 == "2":
        print("You go down the second path.")
        print("Welcome to normal mode, in this mode you keep all your stats from this little tutorial and you get a lv50 weapon of your choice!")
        print("Password for Normal.py:", int(111324))
        hp == hp
        defense == defense
        atk == atk
        speed == speed
        print("Go to github and download the normal.py file.")
        
    elif choice4 == "3":
        print("Bet you were hoping for this huh!")
        print("Welcome to hard mode, in this mode all of your stats are reduced by 10 and it's much harder to play!")
        print("Password for Hard.py:", int(748900))
        hp -= 10
        defense -= 10
        atk -= 10
        speed -= 10
        print("Go to github and download the hard.py file.")
        
    else:
        print("Oh... So you're one of those people...")
        print("You think it's funny that you chose a number other than 1, 2 and 3")
        print("I GOT SOMETHING SPECIAL FOR YOUR ASS MR SMARTASS!!!")
        print("OH SO YOU THINK THIS IS FUNNY, OK WATCH THIS")
        print("WELCOME TO HELL MODE BITCH ALL OF YOUR STATS ARE 5 NOW AND YOU START OFF WITH A POISON EFFECT!!!")
        print("Password for forbidden.py:", int(349825))
        hp = 5
        defense = 5
        speed = 5
        atk = 5
        lv = 1
        print("go to github and open the forbidden.py file(It's packed with refrences)")

if hp == 97 and level <= 2:
    print("You took poison damage")
    hp -= 1
    
print("Current stats: " "Hp", int(hp), "Def", int(defense), "Atk", int(atk), "Spd", int(speed), "Lv", int(level))
