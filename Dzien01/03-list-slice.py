
# Wycinanie elementów listy
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
[ start : stop : step ]
 = start - indeks początkowy
 = stop - indeks końcowy (wyłączony)
 = step - krok (opcjonalny)
"""
print(list1[2:5]) # [3,4,5]
print(list1[4:9]) # [5, 6, 7, 8, 9]
print(list1[4:-1]) # [5, 6, 7, 8, 9]
print(list1[0:3]) # [1, 2, 3]
print(list1[:3]) # [1, 2, 3]
print(list1[7:10]) # 8, 9, 10
print(list1[7:]) # 8, 9, 10
print(list1[-3:]) # 8, 9, 10
print(list1[4::2]) # od wart.5 do końca, co 2-ga wartość
print(list1[::-1]) # symulacja funkcji reverse()