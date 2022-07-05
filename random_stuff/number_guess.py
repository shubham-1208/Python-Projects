from random import randint

first_no = 1

last_no = 1000

number = randint(first_no, last_no)

print("The computer choose a number between", first_no, "and", last_no )

guess = None

while guess != number:
	text = input("Guess the number: ")
	guess = int(text)

	if guess < number:
		print("The number is higher! ")
	elif guess > number:
		print("The number is lower! ")

print("Congratulations you won the game!!!") 
