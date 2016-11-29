class Singer:
	msg = 'Shut up and '
	count = 1
	lst = []

	def __init__(self, name, x):
		self.x = x

	def sing(self):
		Singer.count = Singer.count + 1
		print(self.msg + self.x)
		self.lst.append(self.count)

class Group(Singer):
	def __init__(self, s1, s2):
		self.s1 = s1
		self.s2 = s2

	def sing(self):
		self.count = self.count + 1
		self.s1.sing()
		self.s2.sing()
		self.s1.x, self.s2.x = self.s2.x, self.s1.x
		self.lst.append(self.count)

w_moon = Singer('WALK THE MOON', 'dance')
rihanna = Singer('Rihanna', 'drive')
w_ri = Group(w_moon, rihanna)
w_ri.lst = []

w_moon.sing()
w_ri.s2.sing()
w_ri.sing()
#Group.sing(w_moon)
Group.sing(w_ri)
print(min(rihanna.lst, key=lambda x: -x))
print(w_ri.lst)