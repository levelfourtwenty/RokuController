import sys
from curtsies import Input
from RokuController import sendHttpRequests

def main():
	ip = sys.argv[1]
	actions = sendHttpRequests.requestHandler.actions
	with Input(keynames='curses') as input_generator:
		for keypress in input_generator:
			print(keypress)
			# Checks to see if keypress is a command or is something that is to be used as user text input
			if keypress not in actions:
				sendHttpRequests.requestHandler.sendRequests(keypress, True, ip)
			else:
				sendHttpRequests.requestHandler.sendRequests(actions[keypress], False, ip)
					
	
if __name__ == '__getuserinput__':
	main()
