aliens = 4
password = "aliens"
print("Quickly! aliens are invading the planet!")
print("you need to activate the global defense platformes.")
print("hope you know the password for earths sake...")
print()
print("---------------------------------------------------")
print("     WELCOME TO THE GLOBAL DEFENSE NETWORK         ")
print("---------------------------------------------------")
print()
guess = input("please enter the password: ").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens ** 2
    print("Ther are", aliens, "aliens now on earth. try again.")
    if aliens > 7400000000:
        break
          
    print() 
    print("password hint: the things that are attaking us.")
    print()
    guess = input("Quick enter the password: ")
if aliens > 7400000000:
    print("Nooooooo! the aliens have outnumberd us! all is lost.")
else:
    print("hooray! We won the fight and the world is saved!")
    
    
