import sys

def echo():
	print("Hello")

def hi():
	print("Hey")


def ciao():
	print("ciao")

def say():
	if sys.argv[1]=="Hello":
		echo()
	



if __name__=="__main__":
	say()	
