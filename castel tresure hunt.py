print("Legand has it that, in an anchint castle there is a spechal tresure hidden in the heart of the castle.")
print("as soon as you hear about the castle and get the directions, you get in a car and head over to the castle ASAP.")
print("now you are in the entrance hall of the castle in front of 3 doors")
PlayerChoice = input("Which door do you choose 1,2 or 3?") 
if PlayerChoice == "1":
    print("you walk into door one and find yourself in a room.")
    print("The room is empty ecsept for 2 doors.")
    print("then suddenly,hundreds of bats swarm you!")
    print("1.you can ether try to sckare off the bats,2.run to door one,3.or run")
    print("to door two.")
    BatChoice = input("Which option do you choose?1,2 or 3?")
    if BatChoice == "1":
        print("congratulations!The bats flew away scrambling ovr eachother as they left!")
        print("But, door 1 dissapered!Oh well, you enter door 2 and find another room.")
        print("in the room you find poisinious gas.but,you spot a gas-risistant helmate!")
        print("there is a door at the end of the room.")
        print("you can either,1.take the gas helmate, or 2 hold your breth.")
        GasChoice = input("which option do you choose? 1 or 2?")
        if GasChoice == "2":
            print("you hold your nose and resist the gas. you open the door and you")
            print("find yourself in the tresure room!")
            print("piles and piles of gold serround you.YOU WON!!!")
            exit()
        if GasChoice == "1":
            print("you walk to the helmate and lift it up...")
            print("AND THERS A RATTELSNAKE INSIDE!!!it rears up and bites you. you")
            print("become dizzy and slowley drop to the floor.YOU LOST")
            exit()
    if BatChoice == "2":
        print("you run to door one and jump inside and close the door")
        print("inside, you find yourself in front of stairs and a passageway and a")
        print("bookcase with onley 3 books")
        print("you can:1.go down the stairs,2.go down the hallway, or 3.study the")
        print("books on the bookcase.")
        HallChoice = input("which option do you choose, 1,2, or 3?")
        if HallChoice == "1":
            print("you walk down the steps and find yourself in the castle dungon")
            print("then suddenley THE FLOOR OPENS BENEATH YOU AND YOU FALL TO ")
            print("YOUR DOOM!!!YOU LOST.")
            exit()
        if HallChoice == "2":
            print("you turn down into the hall way and you see red lights in the")
            print("shape of eyes.You turn to run away but its too late. the")
            print("mysterious monster gulps you down in one go.YOU LOSE.")
            exit()
        if HallChoice == "3":
            print("you study the book shelf and you find a sign that sais:")
            print('"you must choose the right book or it will not end well')
            print('you must choose one book."')
            BookChoice = input("wich book do you chooose 1,2, or 3?")
            if BookChoice == "1":
                print("you take the first book off the shelf and open to the first page.")
                print('the first word you see is "WRONG!"')
                print("the room dissolved around you and you fall into empty space.")
                print("YOU LOST.")
                exit()
            if BookChoice == "2":
                print("you take the second book off the shelf and the first words you see")
                print('are:"CORRECT! HORRAY! then the room starts spinning and fades away.')
                print("in the rooms place is mounds of tresure.you found the tresure room! YOU WIN!")
                exit()
            if BookChoice == "3":
                print('"WRONG!"')
                print("then the room starts spinning and you find your self in a a well-lit cavren")
                print("then you hear a ROAR!!! you look op onley to see a DRAGON!!! with one puff of its")
                print("fiery breath, your nothing but a pile of ashes. YOU LOST.")
                exit()
    if BatChoice == "3":
        print("you run to door two but its too late. the bats carry you to a steaming volcano")
        print("then they drop you into the center crater. you fall into the lava and burn to death")
        print("YOU LOST.")
        exit()
if PlayerChoice == "2":
    print("you step into door two and find youself in a room.")
    print("the room is emty ecept for a gold coin on the floor and a door.")
    print('you pick up the gold coin and study it. there is writing on it!')
    print('the writing says "put me in the slot" you wonder "what slot?"')
    print("you can: 1.) look for the mysterious slot or 2.) go into the door.") 
    DoorChoice = input("what do you choose? 1 or two?")
    if DoorChoice == "1":
        print("you search every nook and cranny for a slot than finally after 1 hour,")
        print("you find a small hole just big enough for the coine. you slide the coine into the hole.")
        print('you hear a tiny "click!" then the wall fades away to reveal a secret passageway!')
        print("you walk along the passageway and you find a dooryou open it and another room but this time")
        print("instead of one gold coin there are millions! also, dimonds, rubys, emralds, gems and mounds of other treasure!")
        print("you founs the treasure room!")
        print("YOU WIN!!!!!!!!!")
        exit()
    if DoorChoice == "2":
        print("you walk to the door and open it. inside is a giant pit that seems bottemless! and you are on a small leadge above it!")
        print(" you turn around onley to find stone. the door has dissaperd! luckley, you see a small rope brige.")
        print("that leads to a door on a bigger leadge!")
        print("you can eather 1.)walk across the bridge or 2.)try to find another way across.")
        HoleChoice = input("choose an option. 1 or 2.")
        if HoleChoice == "1":
            print("you step onto the bridge and start walking carfully to the other side. in the middle, you figure out the hard way that")
            print('tiny rope bridges werent bilt for full grown explorors. you hear a "creak" and a "snap", the entire bridge gave way,')
            print(" and you fall to your doom.GAME OVER. YOU LOST.")
            exit()
        if HoleChoice == "2":
            print("you search your tiny leadge for any other way to get across the gap without using that untrustworthy rope bridge.")
            print("finally, after what seemed like forever you find a GRAPPLEING HOOK on the right side of the leadge.")
            print("you throw the grappleing hook up to the cealing. you hear the end of the rope (with the grappple) hook onto the")
            print("cealing. you take one last look at the tiny leadge, say your prayers and swing to the other side.")
            print("you land safley on the leadge with the door. horray! Then you open the door and you find yourself in a room.")
            print("piles and piles of gold and other treasure surround you! you found the treasure room! YOU WIN!")
            exit()
if PlayerChoice == "3":
    print('you open door 3 and steap into a room with nothing but four buttons and a sign that says:"you have to press the correct button or it')
    print('will not end well for you".')
    print('you can 1. press the first button 2. press the second button 3.press the third button 4.press the fourth button or 5.search the room.') 
    
    ButtonChoice = input('wich button or option do you choose? 1,2,3,4 or 5?')
    if ButtonChoice == "1":
        print("you press the first button and the room dissolved around you you find yourselfe inside kiolaia volcano, hwai'i. the volcano")
        print("erupts and you are burned to death by fire, magma and lava.YOU LOST")
        exit()
    if ButtonChoice == "2":
        print("you you press button 2 and you teliport to... SPACE!!! but you did not have a space suit and you could only hold your breath for so long")
        print("but, you see a human rocet zooming tword you! they pick you up and you zoom to mars and start a martion coliny.and you lived happly ")
        print("ever after on the red planet. YOU WIN!")
        exit()
    if ButtonChoice == "3":
        print("you press the third button and the room fades away. in the rooms place is piles and piles of gold and other treasures!")
        print("you found the treasure room!YOU WIN!")
        exit()
    if ButtonChoice == "4":
        print("you press the fourth button and the rooms floor disolved and you fall to your doom.AYEEEEEEEEEE!you yell as you plummet to the")
        print("to the bowls of the earth. YOU LOST.")
        exit()
    if ButtonChoice == "5":
        print("you search and search and search for what seems like forever and then you find a trapdoor. you open it and you find yourself")
        print("in a big room with two doors with writing on it one says: lions and the other says: ?.")
        NameChoice = input("which door do you choose? ?, or lions?")
        if NameChoice == "?":
            print(" you open the door that says ? and you steap into the room onley there is nothing to step on! the floor is a holigram!")
            print(" you fall to your doom.YOU LOST.")
            exit()
        if NameChoice == "lions":
            print(' you open the door that says "lions" and you find, like the door said, a bunch of lions. they attack you.')
            print("but lucly you spot a sword! you pick up the sword and deafeat the lions.you open the door at the other side of the")
            print("room and you find your self in another room. but, the room was full of treasure!you found the treasure room! YOU WIN!!!")
            exit()
        
