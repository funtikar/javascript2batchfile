from sys import *

tokens = []
def buka(argi):
	buff = open(argi,"r").read()
	return buff

def lexer(argi):
	buffa = ""
	str_buff = ""
	str_state = 0
	var_stage = 0
	f_stage = 0
	data = list(argi)
	for aksara in data:
		buffa = buffa + aksara
		#print "current_buffer: " + buffa
		#print var_stage		
		#print tokens


		if (buffa == "print"):
			tokens.append("PRINT")
			buffa = ""
			#print tokens
		if (var_stage == 1 and (aksara == "(" or aksara == ")" or aksara == "{" or aksara == "}" or aksara == "+" or aksara == "-" or aksara == "*" or aksara == "%" or aksara == "$" or aksara == "=" or aksara == "\n" or aksara == " ") ):
			tokens.append("%"+buffa[:-1]+"%")
			buffa = aksara	
			#print tokens
			var_stage = 0
		if (f_stage == 1 and (aksara == "(" or aksara == ")" or aksara == "{" or aksara == "}" or aksara == "+" or aksara == "-" or aksara == "*" or aksara == "%" or aksara == "$" or aksara == "=" or aksara == "\n" or aksara == " ") ):
			tokens.append(buffa[:-1])
			buffa = aksara	
			#print tokens
			f_stage = 0			
		if (buffa == "$"):
			tokens.append("S_VAR")
			buffa = ""
			var_stage = 1
			#print tokens
		if (buffa == "%"):
			tokens.append("N_VAR")
			buffa = ""
			var_stage = 1
		if (buffa == "function"):
			tokens.append("FUNC")
			buffa = ""
			f_stage = 1
		if (buffa == "if"):
			tokens.append("IF")
			buffa = ""			
		if (buffa == "else"):
			tokens.append("ELSE")
			buffa = ""		
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
		if (buffa == "+"):
			tokens.append("PLUS")
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
		if (aksara == " " and str_state == 0):
			tokens.append("WS")
			buffa = ""
		if (aksara == "\n"):
			tokens.append("NEWL")
			buffa = ""
		#print "\n"	
def parser(toki):
	f = open('mojo.bat', 'w')
	f.write("@echo off")
	f.write("\n")
	toktemp = []
	if_state = 0
	for i in range(len(toki)):
		#print toki[i]
		if (toki[i] == "S_VAR" and  toki[i+3] == "EQ" and toki[i+4] != "EQ"):
			f.write("set " + toki[i+1][1:-1])
			i = i + 2
		if (toki[i][0:1] == "%" and toki[i][-1:] == "%"):
			f.write(toki[i])		
		if (toki[i] == "PLUS"):
			f.write("+")
		if (toki[i] == "IF"):
			f.write("if")
			if_state = 1
		if (toki[i] == "EQ"):
			f.write("=")			
		if (toki[i] == "L_CURVE" and if_state !=1):
			f.write("(")	
		if (toki[i] == "R_CURVE" and if_state !=1):
			f.write(")")
		if (toki[i] == "L_CURLY"):
			f.write("(")
		if (toki[i] == "R_CURLY"):
			f.write(")")			
		if (toki[i] == "PRINT"):
			f.write("echo")
		if (toki[i] == "WS"):
			f.write(" ")			
		if (toki[i][0:6] == "STRING"):
			f.write(toki[i][7:])			
		if (toki[i] == "NEWL"):
			f.write("\n")
	f.close()		
def utama():
	lexer(buka("contoh.my"))
	print tokens
	parser(tokens)
	
	
#supposed to be this one down here
#lexer(buka(argv[1]))

utama()
