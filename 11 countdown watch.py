from time import sleep
from playsound import playsound
import glob
import os
from random import randint

secs = int(input('Enter second(s): '))
mins = int(input('Enter minute(s): '))
if mins == 0: 
	while secs != 0:
		print(f'00:{str(secs).zfill(2)}', end='\r')
		# print(str(secs).zfill(2))
		secs -= 1
		sleep(1)
	print(f'00:0{secs}\nAudio ringing...')
	os.chdir(r'M:\Muzik')
	audio = [i for i in glob.glob('*.mp3')]
	random_song = rf'M:\Muzik\\{audio[randint(0,len(audio))]}'
	playsound(random_song)

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
	os.chdir(r'M:\Muzik')
	audio = [i for i in glob.glob('*.mp3')]
	random_song = rf'M:\Muzik\\{audio[randint(0,len(audio))]}'
	playsound(random_song)

