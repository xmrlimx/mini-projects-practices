from time import sleep
from playsound import playsound

secs = int(input('Enter second(s): '))
mins = int(input('Enter minute(s): '))
if mins == 0: 
	while secs != 0:
		print(f'00:{str(secs).zfill(2)}', end='\r')
		# print(str(secs).zfill(2))
		secs -= 1
		sleep(1)
	print(f'00:0{secs}\nAudio ringing...')
	playsound(r'D:\Temp\\newYear.mp3')
	print('Done')


else : 
	while mins >= 1: 
		while secs > -1: 
			print(f'{mins}:{str(secs).zfill(2)}', end='\r')
			secs -= 1 
			sleep(1)
		mins -= 1
		secs += 60
	while secs != 0:
		print(f'00:{str(secs).zfill(2)}', end='\r')
		# print(str(secs).zfill(2))
		secs -= 1
		sleep(1)
	print(f'00:0{secs}\nAudio ringing...')
	playsound(r'D:\Temp\\newYear.mp3')
	print('Done')
