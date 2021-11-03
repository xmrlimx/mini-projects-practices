import random, sys

def roll_dice():
	answer = input('1. Enter\'1\' to roll the dice\n2. Enter \'2\' to exit the program\nYour choice: ')
	try:
		if int(answer) == 1: 
			dice = [i for i in range(1,7)]
			print('','='*20,'\n','='*20,'\n','='*20)
			print(f'    Your result: {random.choice(dice)}')
			print('','='*20,'\n','='*20,'\n','='*20)
			roll_dice()
		elif int(answer) == 2: 
			sys.exit()
		else: 
			print('What the fuck are you trying to do mate? Re-enter \'1\' or \'2\'')
			print('-'*20)
			roll_dice()
	except ValueError: 
		print('What the fuck are you trying to do mate? Re-enter \'1\' or \'2\'')
		print('-'*20)
		roll_dice()
roll_dice()