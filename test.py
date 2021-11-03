from datetime import datetime
from time import sleep

#create get minute function for testing
def get_minutes():
	date = datetime.today()
	return date.strftime('%M')


def track_change():
	initial = get_minutes()
	print('Initial value: %s'% initial)

	track_number = 1
	while track_number < 300:
		current = get_minutes()
		if current != initial:
			print('They value has changed into %s' % current)
		elif current == initial : 
			print('They values are still the same')
		sleep(10)
		track_number += 1
	#sleep(10)
	count += 1



track_change()
