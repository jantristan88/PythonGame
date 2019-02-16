name =input('Name')

print(' Hello, ' + name + '.')

line_1 = " Presidential Election primaries" + " is " + " around the corner."
line_2 = name , 'presidential candidates are looking for a campaign manager, who perfectly fits their vision and background'
line_3 = 'Let us begin in the search for your new boss'


from time import sleep
import sys

for x in (line_1,line_2,line_3):
	print(x, end='',flush=True)  
	sleep(5)


print('Let us begin in the search for your new boss')

import vlc
import time

p = vlc.MediaPlayer("file:///Users/jantristan/Desktop/KickStartCoding/PythonGame/CNN.mp3")
p.play()
time.sleep(60)

candidates = [
	'Donald Trump', 
	'Bernie Sanders', 
	'Joe Biden', 
	'Kamala Harris', 
	'Elizabeth Warren',
	'Cory Booker',
	'Beto ORourke',
	'Julian Castro',
	'Tulsi Gabbard',
	'Amy Klobuchar',
	'Kirsten Gillibrand',]

print(candidates[0])