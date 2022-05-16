import sys
from curtsies import Input
from RokuController import sendHttpRequests
import socket
from pyfiglet import Figlet

def checkValidity(ip):
	try:
		socket.inet_aton(ip)
		return 0
	except socket.error:
		return 1

def main():
	f = Figlet(font='slant')
	print(f.renderText('RokuController'))
	print('\n\n\n')
	if len(sys.argv) != 2:
		raise ValueError("No IP address argument given.")
		exit()
	
	ip = sys.argv[1]
	if checkValidity(ip) == 1:
		raise ValueError("Invalid IP address")
		exit()

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


