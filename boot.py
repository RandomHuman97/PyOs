from time import sleep
import lib_os

print("WELCOME TO PYOS!")
from replit import clear

userfile = open("user.txt", "r+")
data = userfile.read()
if data == "":
    uname = input("Choose a name for PyOs\n")
    userfile.seek(0)
    userfile.write(uname)
    userfile.truncate()
    data = uname


clear()

print("Hi " + data + "!")
userfile.close()
sleep(1)
exec(open("main.py").read()) 
