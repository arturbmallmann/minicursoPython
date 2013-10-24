teste= [2,4,57,3,325,75,123]
def quicksort(l):
	if l:
		pivot = l[0]
		rest = l[1:]#pega de 1 ateh o fim
		smaller= [x for x in rest  if x < pivot]
		bigger= [x for x in rest if x >= pivot]
		return quicksort (smaller) + [pivot] + quicksort (bigger)
	else:
		return []
