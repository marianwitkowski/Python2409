
# Przechtytywanie wyjątków w Pythonie

listA = None
try:
    #open("c:/tmp/test.txt", "rt")
    #x = 1/0
    listA = [1,2,3,4]*1_000_000
    #x = listA[123]
    float("123")
    raise Exception("To jest mój wyjątek")
except OSError as exc:
    print("Wyjątek związany z plikami:",exc)
except (ZeroDivisionError, IndexError) as exc:
    print("Wystąpił wyjątek:", exc)
except Exception as exc:
    print("Jakiś inny wyjątek:", exc)
else:
    print("Wykona się tylko, gdy nie ma wyjątku")
finally:
    print("Zawsze się wykonuje")
    del(listA)