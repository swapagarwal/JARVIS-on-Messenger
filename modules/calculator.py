import math

def process(input, entities):
	output = {}
	try:
		operator = entities['operator']
		firstOp = entities['operand'][0]
		
		output['success'] = True
		
		if (operator == 'sin'):
			output['output'] = math.sin(firstOp)
		elif (operator == 'cos'):
			output['output'] = math.cos(firstOp)
		elif (operator == 'tan'):
			output['output'] = math.tan(firstOp)
		elif (operator == 'asin'):
			output['output'] = math.asin(firstOp)
		elif (operator == 'acos'):
			output['output'] = math.acos(firstOp)
		elif (operator == 'atan'):
			output['output'] = math.atan(firstOp)
		elif (operator == 'sqrt'):
			output['output'] = math.sqrt(firstOp)
		elif (operator == 'ln'):
			output['output'] = math.log(firstOp)
		else:
			secondOp = entities['operand'][1]
			if (operator == '+'):
				output['output'] = firstOp + secondOp
			elif (operator == '-'):
				output['output'] = firstOp - secondOp
			elif (operator == '*'):
				output['output'] = firstOp * secondOp
			elif (operator == '/'):
				output['output'] = firstOp / secondOp
			elif (operator == '%'):
				output['output'] = firstOp % secondOp
			elif (operator == 'pow'):
				output['output'] = math.pow(firstOp, secondOp)
			elif (operator == 'log'):
				output['output'] = math.log(firstOp, secondOp)
			else:
				output['error_msg'] = "I couldn\'t find the result for your calculation"
				output['success'] = False
	
	except:
		output['error_msg'] = "I couldn\'t find the result for your calculation"
		output['success'] = False
	
	
	return output
	
