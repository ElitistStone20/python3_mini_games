from random import shuffle
cards = ['*','&','£']
def welcome():
	cards = ['*','&','£']
	print("Welcome to guess the * game. Hope you lose!")
	player = input("What is your name? ")
	print("Hi! ", player, " the symbols are", cards, "try to find the position of the *")

def startgame(cards):
	lives = 10
	win = 0
	while lives > 0 or win == 1:
		mixed = shuffle(cards)
		choice = int(input("Guess where the star is: "))
		if choice > 2:
			print("only enter either 0, 1 or 2 =_=")
			startgame(cards)
		if cards[choice] == "*":
			win = 1
			print("You won. Somehow!")
			break
		else:
			lives =  lives - 1
			print("Nope not there! You have ",lives, " left!")
welcome()
startgame(cards)
