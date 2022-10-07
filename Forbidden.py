import random
import time

print("Loading Easy.py")
time.sleep(2.4)
print("Dowloading resources")
time.sleep(4.4)
print("Restoring previous data...")
time.sleep(4.4)
print("Checking for bugs...")
time.sleep(3.4)
print("Opening game...")

boldS = '\033[1m'
boldE = '\033[0m'
dice = random.randint(1, 30)
hp = 150
defense = 0
atk = 0
lv = 1
damage = 15
BlueZ = 1000

Password = input("Enter Password: ")
print("Processing")
time.sleep(5.5)
print("loading data")
time.sleep(3.5)
print("Opening files")
time.sleep(3.7)
print("Checking Password")
time.sleep(3)
if Password != "349825":
    Password = "349825"
    print("Wrong password.....")
    time.sleep(1.3)
    print("Correct password entered...")
    time.sleep(2.3)
    print("")

if Password == "349825":
    print("Transferring data..")
    time.sleep(3)
    print("Importing refrences...")
    time.sleep(3)
    print("Adding jokes...")
    time.sleep(3)
    print("Loading....")

    Data = input("Would you like to say anything before we start?: ")
    if Data == Data:
        print("Have fun.. and remem-")
        time.sleep(3.5)
        print("BlueZ: Testing 1...2...Testing...1...2")
        time.sleep(2.3)
        print("BlueZ: alright I've hacked into one of the files....")
        time.sleep(1.7)
        print("BlueZ: Adding in Forbidden.py")
        time.sleep(1.7)
        print("Adding file....")
        time.sleep(1.7)
        print("File added!")
        time.sleep(1.3)
        print("Loading in new data.")
        time.sleep(5.3)



    print("BlueZ's health:", int(10), "BlueZ's Atk:", int(1))
    time.sleep(1)
    print("Current Stats:" "Health:", int(150), "Defense:", int(150), "atk:", int(150))
    time.sleep(1)
    a = input("(Attack) (Defend)")
    if a == "attack":
        print("You attack BlueZ doing 150 damage!")
        time.sleep(1.7)
        print("BlueZ seems unbothered by your attack")
        time.sleep(1.7)
        print("BlueZ attacks you doing 1 damage")
        time.sleep(1.7)
        print("BlueZ yawns as they slowly crack their neck.")
        time.sleep(1.7)
        print("BlueZ looks at their hp bar.")
        time.sleep(1.7)
        print("BlueZ: Man I feel like I'm forgetting something")
        time.sleep(1.7)
        print("BlueZ: Let me change that real quick!")

    elif a == "defend":
        print("You Defend against BlueZ's attack!")
        time.sleep(1.7)
        print("BlueZ attacks you doing 0 damage")
        time.sleep(1.7)
        print("BlueZ yawns as they slowly crack their neck.")
        time.sleep(1.7)
        print("BlueZ looks at their hp bar.")
        time.sleep(1.7)
        print("BlueZ: This isn't right why is it at 10?")
        time.sleep(1.7)
        print("BlueZ: Let me change that real quick!")


    if a == "":
        print("You feel your sins are crawling down your back")
        time.sleep(1.7)
        print("Sans: Hehe.. Hey kid did you hear about the 2 skeletons who got lost in the desert?")
        time.sleep(1.7)
        print("Sans attacks you with a gaster blaster")
        time.sleep(1.7)
        print("You died")
        time.sleep(2.7)
        print("Sans: They were dry as a bone!")
        time.sleep(1.7)
        print("Sans: Woah tough crowd!")
        time.sleep(1.7)
        print("Sans: Guess you can say they lost their funny bone!")
        hp -= hp


if hp <= 0: 
    print("")
else:
    print("")


    print("You feel something bad is about to happen!")
    time.sleep(1.2)
    print("BlueZ: Overriding stat data.")
    time.sleep(1.2)
    print("Initiating data rearrangement....")
    time.sleep(3)
    print("Loading new data....")
    time.sleep(3)
    print("New data loaded!")
    time.sleep(2.2)
    print("BlueZ's health:", int(BlueZ), "BlueZ's Atk:", int(damage))
    time.sleep(1)
    print("Current Stats:" "Health:", int(hp), "Defense:", int(0), "atk:", int(0))
    time.sleep(1)
    a = input("(Attack) (Defend)")
    if a == "attack":
        print("You attack BlueZ doing 0 damage!")
        time.sleep(1.7)
        print("BlueZ: Man hacking into this terminal was hard!")
        time.sleep(1.7)
        print("BlueZ attacks you doing 15 damage to you")
        time.sleep(1.7)
        print("BlueZ: What's wrong... Isn't this what you wanted?")
        time.sleep(1.7)
        print("BlueZ:", boldS, "AFTER ALL ISN'T THAT WHY YOU'RE HERE", boldE)
        time.sleep(1.7)
        print("BlueZ: At this rate you're never gonna drop my hp")
        time.sleep(1.7)
        print("BlueZ: might as well give up... or don't!")
        hp -= 15

    elif a == "defend":
        print("You Defend against BlueZ's attack!")
        time.sleep(1.7)
        print("BlueZ attacks you doing 2.5 damage")
        time.sleep(1.7)
        print("BlueZ: What's wrong not up for the challenge")
        time.sleep(1.7)
        print("BlueZ checks their watch.")
        time.sleep(1.7)
        print("BlueZ: So when are you going to get serious")
        hp -= 2.5


    if a == "":
        print("You hear what sounds like a crowd cheering the name Annie in the distance.")
        time.sleep(1.7)
        print("Annie: This is below my pay grade!")
        time.sleep(1.7)
        print("Annie scoffs before she starts glowing with a rainbow aura")
        time.sleep(1.7)
        print("Annie hits you with the power of a super nova!")
        time.sleep(1.7)
        print("You died")
        time.sleep(1.7)
        print("*Whisper* Annie: Get up I didn't hit you that hard")
        time.sleep(1.7)
        hp -= hp


if hp <= 0: 
    print("")
else:
    print("")


    print("BlueZ's health:", int(BlueZ), "BlueZ's Atk:", int(damage))
    time.sleep(1)
    print("Current Stats:" "Health:", int(hp), "Defense:", int(0), "atk:", int(0))
    time.sleep(1)
    a = input("(Attack) (Defend)")
    if a == "attack":
        print("You attack BlueZ doing 0 damage!")
        time.sleep(1.7)
        print("BlueZ: Guess we're still doing this huh!")
        time.sleep(1.7)
        print("BlueZ attacks you with a computer virus doing 15 damage to you")
        time.sleep(1.7)
        print("BlueZ: Now that I think about it doing 15 damage is kind of low...")
        time.sleep(1.7)
        print("BlueZ: Let me change that!")
        time.sleep(1.7)
        print("BlueZ Attacked you with a computer virus doing 20 damage!")
        time.sleep(1.7)
        print("BlueZ: Much better!")
        hp -= 20

    elif a == "defend":
        print("You Defend against BlueZ's attack!")
        time.sleep(1.7)
        print("BlueZ attacks you doing damage")
        time.sleep(1.7)
        print("BlueZ: ugh stupid glitches")
        time.sleep(1.7)
        print("BlueZ codes a dice simulator.")
        time.sleep(1.7)
        print("BlueZ: Come on baby big number big numbers")
        time.sleep(1.7)
        print("The dice rolls and you take", int(dice), "damage")
        time.sleep(1.7)
        print("BlueZ: not even in the 100's... this sucks!")
        hp -= dice


    if a == "":
        print("The sky goes dark and what looks to be a yellow triangle appears next to you.")
        time.sleep(1.7)
        print("Bill Cipher: Woah am I in a computer!")
        time.sleep(1.7)
        print("Bill Cipher: Why does it just say my name?")
        time.sleep(1.7)
        print("Bill Cipher: It isn't a deal with Stanford but I guess it'll do!")
        time.sleep(1.7)
        print("Bill Cipher: Hey kid wanna make a deal?!")
        time.sleep(1.7)
        print("You nod your head.")
        time.sleep(1.7)
        print("Bill Cipher: If you tell me how to cross over into this dimension!")
        time.sleep(1.7)
        print("Bill holds out his hand.")
        time.sleep(1.7)
        print("Bill Cipher: I'll help you with your little problem there!")
        time.sleep(1.7)
        print("You shook Bill's hand")
        time.sleep(1.7)
        print("Bill Cipher: Hahahaha.. hahahahaha... hahahahaha")
        print("")
        print("            ⢰⡶⢶⡆")
        print("            ⢸⡇⢸⡇")
        print("           ⣀⣼⣇⣸⣧⣀")
        print("           ⠉⢩⡿⢿⡍⠉")
        print("           ⣰⡿⠁⠈⢿⣆")
        print("          ⣴⣿⣥⣤⣤⣬⣿⣦")
        print("         ⣼⡿⠋⠁⢰⡆⠈⠙⢿⣧")
        print("       ⢀⣾⠟⣷⣄ ⠸⠇⠀⣠⣾⠻⣷⡀")
        print("⢀⡀⠀⠀⠀⢠⣾⠋⠀⠀⠙⠛⠿⠿⠛⠋⠀⠀⠙⣷⡄⠀⠀⠀⢀⡀")
        print("⠈⠻⣦⣤⣤⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣤⣤⣴⠟⠁")
        print("   ⣰⣿⣉⣉⣉⣉⣹⣏⣉⣉⣉⣉⣹⣏⣉⣉⣉⣉⣿⣆")
        print("  ⣴⡟⠉⢹⣿⠉⠉⠉⠉⠉⢻⡟⠉⠉⠉⠉⠉⣿⡏⠉⢻⣦")
        print(" ⠐⠛⠛⠛⠛⠛⠛⢻⣿⠛⠛⠛⠛⠛⠛⠻⣿⠛⠛⠛⠛⠛⠛⠂")
        print("⠀⠀⠀⠀⠀⠀⣤⣤⣸⡏⠀⠀⠀⠀⠀⠀⠀⣿⣤⣤⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠉⠙⠁⠀⠀⠀⠀⠀⠀⠀⠙⠉⠁⠀⠀⠀⠀")
        time.sleep(1.7)
        print("You died from being possesed by Bill!")
        hp -= hp


if hp <= 0: 
    print("")
else:
    print("")


    print("Recovering system...")
    time.sleep(1.7)
    print("BlueZ: Overwrite command!")
    time.sleep(1.7)
    print("Overwriting system....")
    time.sleep(3)
    print("Administrator password: ")
    time.sleep(2.1)
    print("BlueZ: Crap forgot about that feature")
    time.sleep(1.3)
    print("*typing*")
    time.sleep(1)
    print("P")
    time.sleep(1)
    print("i")
    time.sleep(1)
    print("n")
    time.sleep(1)
    print("e")
    time.sleep(1)
    print("c")
    time.sleep(1)
    print("o")
    time.sleep(1.4)
    print("Administrator activated...")
    time.sleep(1.4)
    print("Accessing data....")
    time.sleep(3)
    print("Loading previous data...")
    time.sleep(3)
    print("Data loaded.")



    print("BlueZ's health:", int(BlueZ), "BlueZ's Atk:", int(damage))
    time.sleep(1)
    print("Current Stats:" "Health:", int(hp), "Defense:", int(0), "atk:", int(0))
    time.sleep(1)
    a = input("(Attack) (Defend)")
    if a == "attack":
        print("You attack BlueZ doing 0 damage!")
        time.sleep(1.7)
        print("BlueZ: Come on are you even trying?!")
        time.sleep(1.7)
        print("BlueZ attacks you by pressing [ctrl] [alt] [Dele-")
        time.sleep(1.7)
        print("BlueZ: OH COME ON SERIOUSLY")
        time.sleep(1.7)
        print("Updating system")
        time.sleep(5)
        print("kb 175.9/ 7.7 GB")
        time.sleep(1.7)
        print("BlueZ: JESUS CHRIST SCREW THIS I'LL HANDLE IT MYSELF")
        time.sleep(1.7)
        print("BlueZ attacks you with a mouse cursor doing 15 damage")
        hp -= 15

    elif a == "defend":
        print("You Defend against BlueZ's attack!")
        time.sleep(1.7)
        print("BlueZ attacks you doing 12 damage")
        time.sleep(1.7)
        print("BlueZ: Why is this system so hard to hack into!?")
        time.sleep(1.7)
        print("BlueZ's hp dropped to 1 for a second")
        time.sleep(1.7)
        print("You might have a chance at winning this! just hold out!")
        hp -= 12

    if a == "":
        print("A kid with a weird looking watch approaches you")
        time.sleep(1.7)
        print("Ben Tennyson: Woah where am I?")
        time.sleep(1.7)
        print("Ben Tennyson: I knew I shouldn't have eaten all that cake before bed.")
        time.sleep(1.7)
        print("Tennyson turns into an alien and blasts you with fire!")
        time.sleep(1.7)
        print("you died")
        time.sleep(1.7)
        print("Ben Tennyson: did I hit something?")
        hp -= hp


if hp <= 0: 
    print("")
else:
    print("")


    print("Data corrupted")
    time.sleep(5.4)
    print("Restoring previous data....")
    time.sleep(6)
    print("Loading.....")
    time.sleep(7)
    print("Starting system")
    time.sleep(3)
    print("Loading Easy.py")
    time.sleep(3)
    print("Error")
    time.sleep(3)
    print("Closing application......")




if hp <= 0: 
    print("")
else:
    print("")
    
print("First phase of Forbidden.py is complete!")
print("Next Phase will release in a week!")
