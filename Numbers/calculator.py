import sys

def applyOp(op,val1,val2):
	if op == '+':
		return val1+val2
	elif op == '-':
		return val2 - val1
	elif op == '*':
		return val1*val2
	elif op == '/':
		return val2/val1
def hasPrecedence(op1,op2):
	if op2 == '(' or op2 == ')':
		return False
	if (op1 == '*' or op1 == '/') and (op2 == '+' or op2=='-') :
		return False
	return True

def Calculator(inputstr):
	value = []
	operator = []
	i=0
	while i< len(inputstr):
		token = inputstr[i]
		if token == ' ':
			continue
		if token.isdigit():
			number = ''
			while i <len(inputstr) and inputstr[i].isdigit()==True :
				number += inputstr[i]
				i+=1
			i-=1
			value.append(int(number))

		elif token == '(':
			operator.append(token)
		elif token == ')':
			while operator[-1]!= '(':
				value.append(applyOp(operator.pop(),value.pop(),value.pop()))
			operator.pop()
		elif token in '+*-/' :
			while len(operator)!=0 and hasPrecedence(token,operator[-1]):
				value.append(applyOp(operator.pop(),value.pop(),value.pop()))
			operator.append(token)		
		i+=1
#	print operator
	while len(operator)!=0:
		value.append(applyOp(operator.pop(),value.pop(),value.pop()))
	print value[0]
	return;			

def main():
#	print "inside"
	inputStr = raw_input("Enter the expression to calculate \n")	
	Calculator(inputStr)
#	print "outside"
	return
if __name__ == '__main__':
	main()
