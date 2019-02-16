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