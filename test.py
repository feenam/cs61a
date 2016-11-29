def test():
	b = 1
	def ie():
		nonlocal b
		b = 3
		return b
	return ie

y = test()
print(y())