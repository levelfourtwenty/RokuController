from curtsies import Input
import requests
#Change the URL here for this to work with your device, there are many ways to do this, the easiest is to check your router#
url = "http://{YOUR ROKU LOCAL IP HERE}:8060/keypress"
urltyping = "http://{YOUR ROKU LOCAL IP HERE}:8060/keypress/Lit_"

actions = {
	'KEY_UP': 'Up',
	'KEY_DOWN': 'Down',
	'KEY_LEFT': 'Left',
	'KEY_RIGHT': 'Right',
	'\n': 'Select',
	'KEY_HOME': 'Home',
	'KEY_BACKSPACE': 'Backspace',
	'\t', 'Info',
	'\x1b', 'Back'
}

def main():
	try:
		with Input(keynames='curses') as input_generator:
			#this takes input from the user"
			for keypress in input_generator:
				print(keypress)
				#these if statements filter for keys that do certain things on the remote#
				if keypress not in actions:
					requests.post(f'{urltyping}{keypress}')
				else:
					requests.post(f'{url}/' + actions[keypress])
						
	except:
		 exit()
						
if __name__ == '__main__':
	main()
