def check_brackets(brackets):
	stack = []
	for bracket in brackets:
		if bracket in ('{', '[', '('):
			# opening bracket, so push it onto the stack
			stack.append(bracket)
		elif bracket in ('}', ']', ')'):
			try:
				stackBracket = stack.pop()
			except IndexError:
				return False
			if bracket == '}' and stackBracket == '{':
				continue
			if bracket == ')' and stackBracket == '(':
				continue
			if bracket == ']' and stackBracket == '[':
				continue
			return False

	return stack == []