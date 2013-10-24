import functools

class Greeter():
	def __init__(self,gretting):#contrutor, e self é a referencia dele próprio, pode se dar qualquer nome
		self.gretting=gretting

	def greet(self,name):
		print("%s %s!" %(self.gretting,name))
#[x for x in dir (Greeter) if not x.startswith('__')]#mostrar meus metodos

artur=Greeter("olá")

#ou...
def greet(g,name):
	print("%s %s!" %(g,name))

fritz = functools.partial(greet,"Hallo")
