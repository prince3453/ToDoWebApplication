import glob
import time

myfiles = glob.glob("data/*.txt")

for filepath in myfiles:
    with open(filepath, 'w') as f:
        f.write("good")

now = time.strftime("%b %d,%Y %H:%M:%S")
print(now)
print(myfiles)