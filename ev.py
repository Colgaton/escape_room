from evdev import InputDevice, categorize, ecodes, KeyEvent
import os, subprocess


# if wait = 1 it will wait for the song to be played before returning
def playmp3(file,wait=0):
	process = subprocess.Popen(["mpg123", file])
	if wait:
		process.wait()

def main():

	# Code for winning
	solution = "2314"
	player = ""
	# Change this to your setup
	gamepad = InputDevice('/dev/input/event2')

	playmp3("win95.mp3",1)

	for event in gamepad.read_loop():
		if event.type == ecodes.EV_KEY:
			keyevent = categorize(event)
			if keyevent.keystate == KeyEvent.key_down:
				print('Scancode of button pressed: ', keyevent.scancode)
				if keyevent.scancode == 296:
					print('Button 1')
					player = player+"1"
					playmp3("ping.mp3")
				elif keyevent.scancode == 297:
					print('Button 2')
					player = player+"2"
					playmp3("pong.mp3")
				elif keyevent.scancode == 298:
					print('Button 3')
					player = player+"3"
					playmp3("ping.mp3")
				elif keyevent.scancode == 299:
					print('Button 4')
					player = player+"4"
					playmp3("pong.mp3")
		if len(player) == 4:
			if player == solution:
				print("Right solution: ", player)
				playmp3("sirene.mp3",1)
				playmp3("msg2.mp3",1)
				player = ""
			elif player == "1411":
				subprocess.call(["shutdown", "-h", "now"])
			else:
				print("Wrong solution: ", player)
				playmp3("msg1.mp3",1)
				player = ""

main()
