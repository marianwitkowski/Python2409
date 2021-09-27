
# Przykład użycia krotek

x = 10

# przykładowa krotka
result = (200, "OK")
print(type(result))

# krotka 1-elementowa
tuple_1el = ("A",)
print(type(tuple_1el))

# a to nie jest już krotka
tuple_1el = ("A")
print(type(tuple_1el))

# wziąć 2-gi element z krotki result
print(result[1])

# rozkład krotki result do zmiennych
code = result[0] # 1 element krotki
msg = result[1] # 2 element krotki
print(code, msg)

# variable unpacking
code, msg = result # (200, "OK")
print(code, msg, sep=";")

# próba modyfikacji krotki
#result[0] = 300
result = (300, result[1], True )
print(result)

code, msg, _ = result # _ = ślepa zmienna (dummy variable)
print(code, msg)