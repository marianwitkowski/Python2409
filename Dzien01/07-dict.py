
# Słowniki w Pythonie
import json

employee = dict() # pusty słownik
employee = {
    "fname" : "Jan", "lname" : "Kowalski",
    "age" : 44, "manager" : True,
    "acl" : ["Room1", "Room3", "Room9"],
    "car" : {
        "reg_plate" : "WU12345",
        "brand" : "FORD",
        "year" : 2017,
        "mileage" : 156789
    },
}
print(employee["fname"])
print(employee.get("Fname","BRAK IMIENIA"))

# ustawianie kluczy w słowniku
employee["fname"] = "Andrzej"
employee["salary"] = 10_000
employee.update({ "age":45, "manager":False, "acl":[], "notice":1 })
print(employee)

# usuwanie kluczy
del(employee["salary"])
employee.pop("age")
print(employee)

print("Klucze:", employee.keys() )
print("Tylko wartości:", employee.values())
for el in employee.items():
    print(el)

if 'fname' in employee.keys():
    print("Klucz 'fname' istnieje")
if 'fname' in employee:
    print("Klucz 'fname' istnieje")

# Konwersja słownika do JSON string
s = json.dumps(employee)
print(s)
# Konswersja z JSON string do słownika
employee2 = json.loads(s)
print(employee2)
