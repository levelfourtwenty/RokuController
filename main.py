from curtsies import Input
import requests
#Change the URL here for this to work with your device, there are many ways to do this, the easiest is to check your router#
url = "http://YOUR_ROKU_DEVICE_IP:8060/keypress"
urltyping = "http://YOUR_ROKU_DEVICE_IP:8060/keypress/Lit_"
up = f"{url}/Up"
down = f"{url}/Down"
left = f"{url}/Left"
right = f"{url}/Right"
select = f"{url}/Select"
home = f"{url}/Home"
back = f"{url}/Back"
Info = f"{url}/Info"
a = f"{urltyping}a"
b = f"{urltyping}b"
c = f"{urltyping}c"
d = f"{urltyping}d"
e = f"{urltyping}e"
f = f"{urltyping}f"
g = f"{urltyping}g"
h = f"{urltyping}h"
i = f"{urltyping}i"
j = f"{urltyping}j"
k = f"{urltyping}k"
l = f"{urltyping}l"
m = f"{urltyping}m"
n = f"{urltyping}n"
o = f"{urltyping}o"
p = f"{urltyping}p"
q = f"{urltyping}q"
r = f"{urltyping}r"
s = f"{urltyping}s"
t = f"{urltyping}t"
u = f"{urltyping}u"
v = f"{urltyping}v"
w = f"{urltyping}w"
x = f"{urltyping}x"
y = f"{urltyping}y"
z = f"{urltyping}z"
one = f"{urltyping}1"
two = f"{urltyping}2"
three = f"{urltyping}3"
four = f"{urltyping}4"
five = f"{urltyping}5"
six = f"{urltyping}6"
seven = f"{urltyping}7"
eight = "{urltyping}8"
nine = f"{urltyping}9"
zero = f"{urltyping}0"
space = f"{urltyping} "
backspace = f"{url}/Backspace"
#if you want to add more keys go right ahead, I am honestly 
#too lazy to add more now, I've added all of the letters in the 
#latin alphabet and digits 0-10 #
def main():
	try:
		with Input(keynames='curses') as input_generator:
				for keypress in input_generator:
					print(repr(keypress))
					if keypress == ('KEY_UP'):
						requests.post(up)
					if keypress == ('KEY_DOWN'):
						requests.post(down)
					if keypress == ('KEY_RIGHT'):
						requests.post(right)
					if keypress == ('KEY_LEFT'):
						requests.post(left)
					if keypress == ('\n'):
						requests.post(select)
					if keypress == ('KEY_HOME'):
						requests.post(home)
					if keypress == ('/x1b'):
						requests.post(back)
					if keypress == ('/t'):
						requests.post(Info)
					if keypress == ('KEY_BACKSPACE'):
						requests.post(backspace)
					if keypress == ('a'):
						requests.post(a)
					if keypress == ('b'):
						requests.post(b)
					if keypress == ('c'):
						requests.post(c)
					if keypress == ('d'):
						requests.post(d)				
					if keypress == ('e'):
						requests.post(e)
					if keypress == ('f'):
						requests.post(f)
					if keypress == ('g'):
						requests.post(g)
					if keypress == ('h'):
						requests.post(h)
					if keypress == ('i'):
						requests.post(i)
					if keypress == ('j'):
						requests.post(j)
					if keypress == ('k'):
						requests.post(k)
					if keypress == ('l'):
						requests.post(l)
					if keypress == ('m'):
						requests.post(m)
					if keypress == ('n'):
						requests.post(n)
					if keypress == ('o'):
						requests.post(o)
					if keypress == ('p'):
						requests.post(p)
					if keypress == ('q'):
						requests.post(q)
					if keypress == ('r'):
						requests.post(r)
					if keypress == ('s'):
						requests.post(s)
					if keypress == ('t'):
						requests.post(t)
					if keypress == ('u'):
						requests.post(u)
					if keypress == ('v'):
						requests.post(v)
					if keypress == ('w'):
						requests.post(w)
					if keypress == ('x'):
						requests.post(x)
					if keypress == ('y'):
						requests.post(y)
					if keypress == ('z'):
						requests.post(z)
					if keypress == (' '):
						requests.post(space)
					if keypress == ('1'):
						requests.post(one)
					if keypress == ('2'):
						requests.post(two)
					if keypress == ('3'):
						requests.post(three)
					if keypress == ('4'):
						requests.post(four)
					if keypress == ('5'):
						requests.post(five)
					if keypress == ('6'):
						requests.post(six)
					if keypress == ('7'):
						requests.post(seven)
					if keypress == ('8'):
						requests.post(eight)
					if keypress == ('9'):
						requests.post(nine)
					if keypress == ('zero'):
						requests.post(zero)
	except:
		exit()
if __name__ == '__main__':
	main()
