
# Zbiory
import itertools

setA = set()
setA.add(2)

setA = { 1, 2, 1, True, "A", None, False}
print(setA)
#print(setA[0])
for el in setA:
    print(el)

listA = [1,1,2,3,3,4,1,1,4,5,6]
print( list(set(listA)) )

res = itertools.groupby(sorted(listA))
for key, group in res:
    print({ key : len(list(group)) })