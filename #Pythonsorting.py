#Pythonsorting.py

a = [3,4,5,6,777,8,9,6,3,5,7,8,9]

# sorted(a)
a.sort()

print a

a.sort(reverse = True)
print a

tup = (5,6,7,6,7,8,9,3,2,3,4,4,4,4,44444,2,8,9)

sorted(tup)

print tup

def getKey(item):
	return item[0]
l = [[2,3], [6,7], [6,34], [8,98], [1,54]]
print sorted(l, key = getKey)


class Custom(object):
	def __init__(self, name, number):
	self.name = name
	self.number = number

customlist = [
	Custom('object', 99),
	Custom('michael', 1),
	Custom('penguin', 87),
	Custom('life', )
	]

def getKey(custom):
	return custom.number

print sorted(customlist, key = getKey)






