#coding : utf-8

import re

def balancedOrNot(expression) :

    stack = []

    for char in expression :

        if char == '(' :
        	stack.append(char)

        elif char == ')' :
        	if not stack :
        		return False
        	stack.pop()
    return not stack

def isValidOrNot(expression) :
	return re.match(r'^[\d+\-*/\s()]+$', expression)

def evaluate(expression) :

	try :
		result = eval(expression)
		return result

	except ZeroDivisionError :
		return "\t\t\tYou cannot divide by zero\n"

	except SyntaxError :
		return "\t\t\tThere is an operand error\n"

	except Exception as e :
		return "\t\t\tError: {}".format(str(e))

def main() :

	print("\n\t\t\t\t\tCALCULATOR")

	while 1 :

		userInput = input("\n\t\t\tEnter an expression to evaluate or q to quit : ")
		userInput = userInput.strip()

		if userInput.lower() == 'q' :
			break

		if not isValidOrNot(userInput) :

			print("\t\t\tThere is a unsupportable character in your expression.\n")
			continue

		if not balancedOrNot(userInput) :

			print("\t\t\tThe parentheses are not balanced.\n")
			continue

		result = evaluate(userInput)
		print("\t\t\tResult : {}".format(result), "\n")

if __name__ == "__main__" :
	main()