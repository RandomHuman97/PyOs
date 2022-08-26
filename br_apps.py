import lib_os
import lib_exformat
import pathlib
import os
import pc
from replit import clear
sysfiles = [
    "lib_exformat.py", "main.py", "lib_os.py", "br_apps.py", "boot.py",
    "pc.py", "lib_guard.py","os_shell.py"
]
# lists system files to be skipped and not shown


def apprun():
    ran = False
    usin = input("Choose an app to run.\n")
    if os.path.exists(usin):
        ran = True
        import lib_guard
        clear()
        lib_guard.safescan(usin)
        exec(open(usin, encoding="utf8").read())
    elif ran == False:
        print("Invalid file")


lib_os.mainheader()
print(pc.RED + "APPS:" + pc.ENDCOLOR)
print(pc.PINK)
for entry in os.scandir():
    if pathlib.Path(os.getcwd() + entry.name).suffix == ".py":
        if not entry.name in sysfiles:
            print(entry.name)
print(pc.ENDCOLOR)
apprun()
