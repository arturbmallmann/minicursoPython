#!/usr/bin/python3
class ExplosionError(Exception):
    pass

def blow_up():
    print("Boom!")
    #raise ExplosionError()

try:
    blow_up()
except ExplosionError:
    print("The function crashed beautifully!")
else:
    print("Oh no, the program didn't crash!")
finally:
    print("I will run unconditionally. :D")
