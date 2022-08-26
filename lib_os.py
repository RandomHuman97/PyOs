import lib_exformat
import os
import sys
import time as t
import pc
from replit import clear
# colors:


def mainheader():
    clear()
    print(pc.YELLOW+"Py"+pc.CYAN+"Os"+pc.GREEN+" V1.0", end="")
    print(pc.RED+"    0.START    1.APPS    2.EXIT", end="")
    print(pc.GREEN+"    ")
    print(pc.ENDCOLOR)


def taskinp():
    wheretogo = input("Choose which task to go to.\n")

    def switchfocus():
        args = ['0', '1', '2']
        checkran = False
        if wheretogo == '0':
            checkran = True
            exec(open("main.py").read())
        if wheretogo == '1':
            checkran = True
            exec(open("br_apps.py").read()) 
        if wheretogo == '2':
            clear()
            print("Goodbye!")
            checkran = True
            sys.exit()
        elif wheretogo not in args:
            if checkran == False:
                print("Invalid statement!")
                taskinp()
    switchfocus()


def exitfile():
    print("\n\n"+pc.CYAN+"Returning to OS..."+pc.ENDCOLOR)
    t.sleep(3)
    exec(open("main.py").read())


