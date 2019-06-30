from tkinter import *
import random

successRateCounter = 0
result = 0
randomChecker = False

levelRange = 4
randomNumber = random.randint(1,levelRange)
randomNumber2 = random.randint(1,levelRange)

answer = randomNumber * randomNumber2

#Method used to take a users selection of a game mode they would like to play, carries out various methods depending on the input
def mainMenu():
    
	gameSelect = input("\nSelect one of the following options:\n (1)Addition \n (2)Subtraction \n (3)Multiplication \n (4)Division \n (5)Random sums \n (6)Quit\n")
	gameSelect = inputChecker(gameSelect)

	if(gameSelect == 1 or gameSelect == 2 or gameSelect == 3 or gameSelect == 4 or gameSelect == 5):
		game(gameSelect)

	elif(gameSelect == 6):
		exit()

	else:
		print("That value was not a selectable choice, please enter the a valid value")
		mainMenu()

	
#Method used to check that a users input is a valid whole integer when entered 	
def inputChecker(userInput):
	try:
		userInput = int(userInput)

	except ValueError:
		userInput = inputChecker(input("\nPlease enter a valid entry: "))
		
	return userInput


#Method that runs a an arithmetic game by using the user's input as a parameter
#Each time an iteration of the method is ran via recursion 2 random numbers are generated for the calculation
#This method also uses 2 other methods to dynamically change the difficulty of the game based on the player's success
def game(gameType):
	global successRateCounter
	global result
	global levelRange
	global randomChecker

	randomNumber = random.randint(1,levelRange)
	randomNumber2 = random.randint(1,levelRange)

	if(gameType == 1):
		result = randomNumber + randomNumber2
		print("\nWhat is the total of the listed numbers when added?\n")
		
	if(gameType == 2):
		result = randomNumber - randomNumber2
		
		if(result < 0):
			game(2)
		else: 
			print("\nWhat is the total of the second number subtracted from the first number?\n")
			
	if(gameType == 3):
		result = randomNumber * randomNumber2
		print("\nWhat is the total of the listed numbers when multiplied?\n")
		
	if(gameType == 4):
		result = randomNumber / randomNumber2
		
		if(result.is_integer() == False):
			game(4)
			
		else:
			print("\nWhat is the total of the first number divided by the second number?\n")
			
	if(gameType == 5):
		randomChecker = True
		game(random.randint(1,4))
			
	print(randomNumber,"and",randomNumber2,"\n")
	userInput = input()
   
	userInput = inputChecker(userInput)
    
	if(randomChecker == True):
		gameType = 5
	
	if(result == userInput):
		recur = input("\nThat is correct, well done! Press Y to try the same operation or N to stop: ")
			
		if(recur == "Y" or recur == "y"):
			
			successRateCounter += 1
			
			if(successRateCounter == 3):
				makeHarder()
				print("\nThe game difficulty has increased since you got 3 answers in a row correct!")
				successRateCounter = 0	
	
			game(gameType)
				
		elif(recur == "N" or recur == "n"):
			levelRange = 4
			mainMenu()
						
		else: 
			print("\nThat was an invalid entry")
			levelRange = 4
			mainMenu()
			
	else:
		print("\nNot right, the correct answer is: ", int(result))
		recur = input("\nPress Y to try the same operation or N to stop: ")
		
		if(recur == "Y" or recur == "y"):
		
			successRateCounter -=1
			
			if(successRateCounter == -3):
				makeEasier()
				print("\nThe game difficulty has decreased since you got 3 answers in a row wrong")
				successRateCounter = 0
				
			game(gameType)
			
		elif(recur == "N" or recur == "n"):
			levelRange = 4
			mainMenu()
			
		else:
			print("\nThat was an invalid entry \n")
			levelRange = 4
			mainMenu()


#Method that increases the difficulty of the game based on how many questions the user gets right
def makeHarder():
	
		global levelRange
		levelRange += 1

#Method that decreases the difficulty of the game based on how many questions the user gets wrong
def makeEasier():

		
        global levelRange
        levelRange -= 1
		


mainMenu()
