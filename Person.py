from datetime import datetime
class Person():
	def __init__(self,name,birthdate,address):
		self.name=name
		self.birthdate=birthdate
		self.address=address
	
	def introduceSelf(self):
		print("hello, my name is %s!" %(self.name))

	def age(self):
		age=datetime.now() - self.birthdate
		days=age.days/365
		return days


artur=Person("artur",datetime(1991,2,27),"blablabla")
joaozinho=Person("jojo",datetime(1992,12,22),"blablabla")
digo=Person("rodrigo",datetime(1,12,22),"blablabla")
