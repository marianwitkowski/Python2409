import math

# Iteracja i przeglądanie list
list1 = [2, 5, -10, -12.3, -65.33, 123, 986, -8321 ]
for i in range(len(list1)):
    print(list1[i], end="; ")
print()

# filtrowanie listy
result = []
for counter,x in enumerate(list1, 1):
    print(f"Pozycja {counter} = {x}")
    if x>0:
        result.append(x)

print()
print("Wynik:", result)

# Wyrażenie listotwórcze
result = [x**3 for x in list1 if x>0]
print(result)

# Funkcja filter()
def gt0(x):
    return x>0

print(list(filter(gt0, list1)))
print(list(filter(lambda x:x>0, list1)))

# Funkcja map()
def mul2(x):
    return x*2

print(list(map(mul2, list1)))
print(list(map(lambda x:x*2, list1)))

### Dodawnie wartosci listy na podstawie indeksów
listA = [1,2,3,4,5]
listB = [-1,-2,-3,-4,-5]
result = []
for x,y in zip(listA, listB):
    result.append(x+y)
print(result)

result = [x+y for x,y in zip(listA,listB)]
print(result)

print(listA + listB)
print(listA*2)
print([False]*40)
