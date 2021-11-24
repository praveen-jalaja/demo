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
	elif sys.argv[1]=="hey":
		hi()
	
	



if __name__=="__main__":
	say()	
