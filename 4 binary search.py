import random

binary = [i for i in range(1,101)]
random.shuffle(binary)
user_input = int(input('Number to lookup: '))
try:
	index = binary.index(user_input)
	print(f'Found {user_input} at location {index}')
except ValueError:
	print(f'Can\'t find {user_input} in the list')