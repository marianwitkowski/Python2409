
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

#shutil.