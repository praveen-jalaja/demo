import sys

def echo():
	print("Hello")


def default():
	print("vannakam")


def hi():
	print("Hey")


def ciao():
	print("ciao")

def say():
	if sys.argv[1]=="Hello":
		echo()
	elif sys.argv[1]=="hey":
		hi()	
	else:
		default()



if __name__=="__main__":
	say()	
