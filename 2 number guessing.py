import random , sys

def guessing_game():
	number = random.choice([i for i in range(1,10)])
	guessed = []
	def user_input_guess():
		while len(guessed) < 3:
			user_guess = int(input('Enter your guess: '))
			if len(str(user_guess)) > 1:
				print('Please enter number from 1 -> 9 onleh! Please try again')
				user_input_guess()
			else:
				guessed.append(user_guess)
	user_input_guess()

	print(f'You guessed the right one. The lucky number is {number}' if number in guessed else f'Wrong. The lucky number is {number}')

guessing_game()