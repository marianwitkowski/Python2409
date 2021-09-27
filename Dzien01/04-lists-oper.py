
# Kopiowanie/sortowanie/zmiana kolejności

list1 = [1,2,3,4,5]
list2 = list1.copy() # poprawne kopiowanie/klonowanie tablic
list1[0] = list1[0]*(-1)
print(list1, list2)
print( id(list1), id(list2) )

list2 = [100, -10, 1, 2, 3, 10, 5, 7.8, 11]
list2.sort()
print(list2)

list2 = [100, -10, 1, 2, 3, 10, 5, 7.8, 11]
list2.sort(reverse=True)
print(list2)

list2 = [100, -10, 1, 2, 3, 10, 5, 7.8, 11]
list2.reverse()
print(list2)

print("="*60)
list2 = [100, -10, 1, 2, 3, 10, 5, 7.8, 11]
print( sorted(list2, reverse=True) )
print(list2)

def scores_compare(x):
    return x[1]

# Sortowanie na podstawie własnej funkcji porównującej
print("="*60)
scores = [ ('Jan',4.5) , ('Mirek', 3.9), ('Piotr', 4.99), ('Kasia', 4.65) ]
print(sorted(scores, reverse=True, key=scores_compare))
print(sorted(scores, reverse=True, key=lambda x:x[1]))


