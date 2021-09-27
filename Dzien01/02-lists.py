
# Listy w Pythonie

empty_list = []
empty_list = list()

list1 = [1, 123.45, "ABC", False, (-1,1), [1,2,3], None]
print("Liczba elementów w liście to", len(list1))
print("Liczba elementów w liście to "+ str(len(list1)) )
print(f"Liczba elementów w liście to {len(list1)}" )

print(list1[5], list1[-2] ) # element przedostatni
print(list1[1], list1[-6] ) # element 2-gi

"""
list1[0] = None
list1[-1] = 1
"""
list1[0], list1[-1] = None, 1
list1[0] = None; list1[-1] = 1
print(list1)

# Operacje na listach
list1.append("Hello world!") # dodanie pojedynczej wartosci
list1.extend([7,8,9]) # dodanie innej listy do list1
list1.insert(1, 678) # wstawienie na 2-giej pozycji listy
list1.remove("Hello world!") # usuwanie na podstawie wartości

if "XYZ" in list1:
    list1.index("XYZ") # indeks 1-go wystapienia
    list1.remove("XYZ") # usuwanie na podstawie wartości

del(list1[1]) # usuwanie na podstawie indeksu listy
x = list1.pop(-2) # zdejmuje przedostatnią wartość
print(x, list1)