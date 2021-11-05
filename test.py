import random 
from word_list import words


random_word = words[random.randint(0,len(words) - 1)]
# random_word = 'Banana'
print('Guess the word: ')
hidden_word = []
for i in random_word:
	if i != ' ':
		hidden_word.append('_ ')
	else: 
		hidden_word.append(' ')
print(' '.join(hidden_word))

count = 1
all_guess = []
track_number = 7
while '_ ' in hidden_word and count < track_number + 1:
	user_guess = input('Guess a letter baby: ')
	print('Please enter only 1 letter at a time!!!'.upper() if len(user_guess) > 1 else '')
	corrected_guess = []
	if user_guess in random_word.lower(): 
		for index, elements in enumerate(random_word.lower()):
			if user_guess == elements: 
				corrected_guess.append(index)
		all_guess.append(user_guess)
		for i in corrected_guess: 
			hidden_word[i] = f'{user_guess} '
		print(f'Letters you have guessed {" ".join(all_guess)}')
		print(' '.join(hidden_word))
	else:
		all_guess.append(user_guess)
		print('-'*50)
		print(f'Letters you have guessed {" ".join(all_guess)}')
		print('There\'s no %s' % user_guess)
		print(f'You only have {track_number - count} lives left' if (track_number - count > 1) else 'You only have 1 live left, you fucking stoooopid')
		print('-'*50)
		count += 1
		print(' '.join(hidden_word))
print('You got it: "%s"' %random_word if count < track_number else f"You didn't get it, you bastard. It was {random_word}")	



"""for index, elm in enumerate(random_word.lower()):
					if user_guess == elm : 
						corred_guess.append(index)
						for i in corred_guess:
							hidden_word[i] = f'{user_guess} '
							print(' '.join(hidden_word))
					elif user_guess != elm: 
						count += 1 
						for i in corred_guess:
							hidden_word[i] = f'{user_guess} '
							print(' '.join(hidden_word))"""

