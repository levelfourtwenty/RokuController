import requests
import os

class requestHandler:
	actions = {
	'KEY_UP': 'Up',
	'KEY_DOWN': 'Down',
	'KEY_LEFT': 'Left',
	'KEY_RIGHT': 'Right',
	'\n': 'Select',
	'KEY_HOME': 'Home',
	'KEY_BACKSPACE': 'Backspace',
	'\t': 'Info',
	'\x1b': 'Back',
	'+': 'VolumeUp',
	'-': 'VolumeDown',
	'KEY_DC': 'PowerOff'
	}
	# The final three actions are specific to Roku TVs and therefore may not work on some devices

	def sendRequests(keypress, typing, var):
		ip = var
		# Checks environment variable to see if it is set, raises if not set
		try:	
		# filters off user input into typed input and non-typed input and requests accordingly
			if typing == True:
				request = f"http://{ip}:8060/keypress/Lit_{keypress}"
				requests.post(request)
			else:
				request = f"http://{ip}:8060/keypress/{keypress}"
				requests.post(request)	
			return 0
	
		except Exception as e:
			print(e)
			return 1
			# miscellanious exception handling

		
	
