import random 

def pass_generator():
	length_ = int(input('Enter the password length you would like to generate:\n> '))
	char = '`~1!2@3#4$5%6^7&8*9(0)-_=+}]{[pPoOiIuUyYtTrReEwWqQaSdDfFgGhHjJkKlL;:"zxcvZXCVbBnNmM,<.>/?'
	chars = [i for i in char]
	random.shuffle(chars)
	print(f'Your new password: {"".join(chars[0:length_])}')

pass_generator()