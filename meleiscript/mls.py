from sys import *

tokens = []
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
			#print "[debugging] it was a print"
			buffa = ""
		if (buffa == "if"):
			tokens.append("IF")
			buffa == ""
		if (buffa == "("):
			tokens.append("L_CURVE")
			buffa == ""
		if(aksara == "\""):
			#print "[debugging] it was a string!"
			if (str_state == 0):
				str_state = 1
			elif (str_state == 1):
				str_state = 0
				str_buff = buffa
				tokens.append(buffa[1:-1])
				buffa = ""
		if (aksara == " " and str_state == 0):
			buffa = ""
		if (aksara == "\n"):
			buffa == ""
def utama():
	lexer(buka("contoh.my"))
	print tokens
	
#supposed to be this one down here
#lexer(buka(argv[1]))

utama()
