def soma (collection):#se um argumento tiver valor padrao os proximos tbm devem ter
    total = 0
    for item in collection:
        total += item
    return total
def soma2 (x):
    return x + 2

#print( list( map ( double, [3,4,5])))

def par(x):
    return x % 2 == 0


print(all(map(par,[2,4])))
print(all(map(par,[2,3])))

