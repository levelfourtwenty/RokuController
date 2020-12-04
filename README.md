# RokuController
This is the result of me losing my remote :)

# What is this program and how do I use it?
This program takes Keyboard input from a user when ran, it allows for entry of words, navigation around applications via any computer on the same network as the device, I decided to develop it as I saw a lack of programs to control roku devices via a computer.

The Keybinds are as follows.

Arrows - Simple movement, you will be able to figure this out. 
Escape - Back
Ctrl+I - Info
select - Enter
Home - Home Key

More are to come, This was enough to navigate the menus for the period of time that I used it'll be fine for now. 

# Dependencies and Setup

The script relies on the requests module and curtsies.

To install them run `pip3 install -r requirements.txt` on the provided text file; pip will install the requirements for you.

Then find the local IP Address of the device, there are several ways of doing this, the easiest way to do so would be checking the connected devices via your router admin panel, 
if this isn't possible refer to the first section of [this](https://developer.roku.com/en-ca/docs/developer-program/debugging/external-control-api.md) article by Roku.

Change these two lines of code to the local ip address of the device.
```python
> url = "http://YOUR_ROKU_DEVICE_IP:8060/keypress"
> urltyping = "http://YOUR_ROKU_DEVICE_IP:8060/keypress/Lit_"
```
Now when you run the script it should work. Do so by running `python3 main.py`

# How does this script work?

The script sends requests (via the request module) to the roku device when you press keys. 

# "But you should've done this not this" 
I am not the best programmer in the world, if you have a suggestion leave an issue and I will get to it other then that, enjoy your new remote.


also inb4 roku dmca
