
# Funkcje
import math

def dummy_function():
    pass

def calculate_circle_area(r : float) -> float:
    return r**2 * math.pi

def calculate_circle_circ(r : float) -> float:
    return 2*math.pi*r

def calculate_circle(r):
    return calculate_circle_area(r), calculate_circle_circ(r)

print(calculate_circle(2))

# Paramtery opcjonalne
def create_employee(fname, lname, phone="601602603", email="biuro@firma.pl"):
    return {
        "fname" : fname, "lname": lname, "phone" : phone, "email":email
    }

print(create_employee("Jan","Kowalski","678123456", "jk@firma.pl"))
print(create_employee("Jan","Kowalski"))
print(create_employee("Jan","Kowalski", phone="501111222"))
print(create_employee("Jan","Kowalski", "501111222"))
print(create_employee("Jan","Kowalski", email="jk1@firma.pl"))
print(create_employee("Jan","Kowalski", email="jk1@firma.pl", phone="555111222"))

# Funkcja z nieustaloną liczbą argumentów
def many_arguments(par1, *args):
    print(f"Parametr obowiązkowy = {par1}")
    for index, arg in enumerate(args,1):
        if type(arg) in [str, int]:
            print(f"Argument #{index} = {arg}")

print("="*60)
many_arguments("Jan","Kowalski","Marian","Krzaklewski", (-1,1) )
print("="*60)
many_arguments(1,2,3,4,5,6,7,"X",False,876.12)

# Funkcja z parametrami nazwanymi
def create_employee2(**kwargs):
    print("=" * 60)
    print(f"Imie={kwargs.get('fname')}")
    print(f"Nazwisko={kwargs.get('lname')}")
    print(f"Wiek={kwargs.get('age')}")
    print(f"Manager={kwargs.get('manager')}")
    print(f"Departament={kwargs.get('deparment')}")


create_employee2(fname="Jan",lname="Kowalski",age=45)
create_employee2(fname="Jan",manager=True, lname="Kowalski",age=45)
create_employee2(fname="Jan",lname="Kowalski", deparment="IT" )

# Funkcja anonimowa/wyr. lambda
print("="*60)
x = lambda a: a+100
y = lambda a,b: [a,b]
print(x(10))
print(y("A","B"))

# Widoczność zmiennych
global_var = 10

def change_global_var(x):
    global global_var
    global_var = x

print("="*60)
print(global_var)
change_global_var(-10)
print(global_var)
