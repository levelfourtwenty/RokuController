from curtsies import Input
import RokuController

def main():
	actions = RokuController.requestHandler.actions
	with Input(keynames='curses') as input_generator:
		for keypress in input_generator:
			print(keypress)
			# Checks to see if keypress is a command or is something that is to be used as user text input
			if keypress not in actions:
				RokuController.requestHandler.sendRequests(keypress, True)
			else:
				RokuController.requestHandler.sendRequests(actions[keypress], False)
					
	
if __name__ == '__rokucontroller__':
	main()
