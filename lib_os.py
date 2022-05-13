import lib_exformat
import os
import sys
import time as t
import pc
# colors:


def mainheader():
    lib_exformat.linespace(10)
    print(pc.YELLOW+"Py"+pc.CYAN+"Os"+pc.GREEN+" V1.0", end="")
    print(pc.RED+"    0.START    1.APPS    2.EXIT", end="")
    print(pc.GREEN+"    by human0")
    print(pc.ENDCOLOR)


def taskinp():
    wheretogo = input("Choose which task to go to.\n")

    def switchfocus():
        args = ['0 ', '1 ', '2 ']
        checkran = False
        if wheretogo == '0':
            checkran = True
            exec(open("main.py").read())
        if wheretogo == '1':
            checkran = True
            exec(open("br_apps.py").read())
        if wheretogo == '2':
            lib_exformat.linespace(10)
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


def safescan(filen):
    with open(filen, encoding="utf8") as file_in:
        drcheck = ""
        for line in file_in:
            drcheck = drcheck + line
        drcheck = drcheck.lower()
        oscheck = "os.remove"
        oscheckforsneakybypassesbydumbpeople = "import os as"
        if 'fernet' in drcheck or 'shutil.rmtree()' in drcheck or oscheck in drcheck or oscheckforsneakybypassesbydumbpeople in drcheck or "=open(" in drcheck.strip().lower():
            print(pc.PURPLE+"***********************************\nWARNING\nTHIS FILE IS NOT SAFE\nIT MOST LIKELY CONTAINS MALWARE\n***********************************\n\n\n\n\n\n\n\n\n\n\n\n")
            # pass compiler error to halt all functions
            raise Exception(
                "Killed proccess due to antivirus while trying to open "+file_in)
