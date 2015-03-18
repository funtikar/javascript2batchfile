from sys import *

def buka(argi):
	buff = open(argi,"r").read()
	return buff

def lexer(argi):
	buffa = ""
	str_buff = ""
	str_state = 0
	data = list(argi)
	for aksara in data:
		buffa = buffa + aksara
		if (buffa == "print"):
			print "[debugging] it was a print"
			buffa = ""
		if (buffa == "if"):
			if (if_state == 0):
				if_state = 1
		if (if_state == 1 and buffa == "("):
			
		if(aksara == "\""):
			print "[debugging] it was a string!"
			if (str_state == 0):
				str_state = 1
			elif (str_state == 1):
				str_state = 0
				str_buff = buffa
				buffa = ""
				print str_buff
		if (aksara == " " and str_state == 0):
			buffa = ""
def utama():
	lexer(buka("contoh.my"))
	
#supposed to be this one down here
#lexer(buka(argv[1]))

utama()
