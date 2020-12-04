from curtsies import Input
import requests
#Change the URL here for this to work with your device, there are many ways to do this, the easiest is to check your router#
url = "http://{YOUR ROKU LOCAL IP HERE}:8060/keypress"
urltyping = "http://{YOUR ROKU LOCAL IP HERE}:8060/keypress/Lit_"

def main():
	try:
		with Input(keynames='curses') as input_generator:
			for keypress in input_generator:
				print(keypress)
				if keypress == ("KEY_UP"):
					requests.post(f"{url}/Up")
				if keypress == ("KEY_DOWN"):
					requests.post(f"{url}/Down")
				if keypress == (f"KEY_LEFT"):
					requests.post(f"{url}/Left")
				if keypress == (f"KEY_RIGHT"):
					requests.post(f"{url}/Right")
				if keypress == (f"\n"):
					requests.post(f"{url}/Select")
				if keypress == (f"KEY_HOME"):
					requests.post(f"{url}/Home")
				if keypress == (f"KEY_BACKSPACE"):
					requests.post(f"{url}/Backspace")
				if keypress == (f"\t"):
					requests.post(f"{url}/Info")
				if keypress == (f"\x1b"):
					requests.post(f"{url}/Back")

				else: 
					requests.post(f"{urltyping}{keypress}")
						
	except:
		 exit()
						
if __name__ == '__main__':
	main()
