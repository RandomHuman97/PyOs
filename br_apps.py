import lib_os
import lib_exformat
import pathlib
import os
import pc
sysfiles=["lib_exformat.py","main.py","lib_os.py","br_apps.py","boot.py","pc.py"]
#lists system files to be skipped and not shown
def apprun():
  ran = False
  usin = input("Choose an app to run.\n")
  if os.path.exists(usin):
      ran = True
      lib_exformat.linespace(10)
      exec(open(usin).read())
  elif ran == False:
    print("Invalid file")
    #TODO: make input repeat until vaild file
lib_os.mainheader()
print(pc.RED+"APPS:"+pc.ENDCOLOR)
print(pc.PINK)
for entry in os.scandir():
    if pathlib.Path(os.getcwd()+entry.name).suffix == ".py":
      if not entry.name in sysfiles:
        print(entry.name)
print(pc.ENDCOLOR)
apprun()