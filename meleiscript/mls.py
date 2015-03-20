from sys import *

tokens = []
def buka(argi):
	buff = open(argi,"r").read()
	return buff

def lexer(argi):
	buffa = ""
	str_buff = ""
	str_state = 0
	svar_state = 0
	nvar_state = 0
	f_state = 0
	data = list(argi)
	for aksara in data:
		buffa = buffa + aksara
		print buffa
		if (buffa == "print"):
			tokens.append("PRINT")
			#print "[debugging] it was a print"
			buffa = ""
		if (buffa == "$"):
			svar_state = 1		
		if (buffa == "%"):
			nvar_state = 1			
		if (buffa == "if"):
			tokens.append("IF")
			buffa = ""
		if (buffa == "function"):
			f_state = 1
			#tokens.append("FUNC")		
		if (buffa == "="):
			tokens.append("EQ")
			buffa = ""
		if (buffa == "!"):
			tokens.append("NOT")
			buffa = ""
		if (buffa == ">"):
			tokens.append("GTHAN")
			buffa = ""
		if (buffa == "<"):
			tokens.append("LTHAN")
			buffa = ""			
		if (aksara == "(" and f_state == 2):
			tokens.append(buffa[:-1])
			tokens.append("L_CURVE")
			buffa = ""
			f_state = 0
		if (buffa == "("):
			tokens.append("L_CURVE")
			buffa = ""
		if (buffa == ")"):
			tokens.append("R_CURVE")
			buffa = ""
		if (buffa == "{"):
			tokens.append("L_CURLY")
			buffa = ""					
		if (buffa == "}"):
			tokens.append("R_CURLY")
			buffa = ""		
		if(aksara == "\""):
			#print "[debugging] it was a string!"
			if (str_state == 0):
				str_state = 1
			elif (str_state == 1):
				str_state = 0
				str_buff = buffa
				tokens.append("STRING:" + buffa[1:-1])
				buffa = ""
		if (aksara == " " and str_state == 0 and svar_state == 0 and nvar_state == 0 and f_state == 0):
			buffa = ""
		elif (aksara == " " and svar_state == 1):
			tokens.append("S_VAR:" + buffa[1:])
			buffa = ""
			svar_state = 0
		elif (aksara == " " and nvar_state == 1):
			tokens.append("N_VAR" + buffa[1:])
			buffa = ""
			nvar_state = 0
		elif (aksara == " " and f_state == 1):
			tokens.append("FUNC")
			buffa = ""
			f_state = 2
		if (aksara == "\n"):
			buffa = ""
def utama():
	lexer(buka("contoh.my"))
	print tokens
	
#supposed to be this one down here
#lexer(buka(argv[1]))

utama()
