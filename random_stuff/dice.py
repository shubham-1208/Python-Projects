import random

def roll(sides=6) :
    num_rolled = random.randint(1,sides)
    return num_rolled

def main() :
    sides =6
    rolling = True
    while rolling:
        roll_again = input("Ready to ROLL? ENTER=Roll Q=Quit. ")
        if roll_again.lower() != "q" :
            num_rolled = roll(sides)
            print("you rolled a", num_rolled)

        else :
            rolling = False
main()

print("Thanks for playing.")
