
import vlc
p = vlc.MediaPlayer("CNN.mp3")
p.play()

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