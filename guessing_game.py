import random
correct_answer = random.randint(1,4)

#print(correct_answer)

in_number = input("Guess the number :")

#print(in_number)

if str(correct_answer) == str(in_number) :
    print("Hurray you guessed right ans!!")

else :
    print("Better luck next time  :)")
print("The number was " + str(correct_answer))



#noun1 = input("Give me a noun :")
#noun2 = input("give another noun :")
#print("fuck you " + noun1 + ", let me eat that " + noun2)
