
# Operacje na plikach i katalogach
import os
import shutil
import glob

print("Bieżący katalog:", os.getcwd())
print("Listowanie: ", os.listdir("."))
print("Tylko pliki PY:", glob.glob("./**/*.py", recursive=True) )
if not os.path.exists("tmp"):
    os.mkdir("tmp")
else:
    os.removedirs("tmp")

curr_dir = os.getcwd()
file_name = curr_dir + "/" + "test.txt"
file_name = curr_dir + os.sep + "test.txt"
file_name = os.path.join(curr_dir, "test.txt")
print(file_name)

if os.path.exists("test.txt"):
    os.unlink("test.txt")

shutil.copy("09-filesystem.py","test.py")

# Praca z plikami tymczasowymi
import tempfile
print("Tmp folder:", tempfile.gettempdir())
with tempfile.NamedTemporaryFile("wt", delete=True) as fd:
    print(fd.name)
    fd.write("Linia 1\r\n")
    fd.write("Linia 2\r\n")
    fd.flush()
    fd.write("Linia 3\r\n")
print("Pliki tymczasowe usunięte")

with tempfile.TemporaryDirectory() as tmp_dir:
    print(tmp_dir)
    file_name = os.path.join(tmp_dir, "log.txt")
    with open(file_name, "wt") as fd:
        fd.write("645645646456456675675")
        fd.flush()

print("Folder usunięty")

