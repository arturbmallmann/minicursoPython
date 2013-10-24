from collections import namedtuple

a=namedtuple('ponto',['x','y'])
a.ponto=3,2
#a.ponto pegar o valor

#exemplo extendendo a

class Vector(a):
	pass
