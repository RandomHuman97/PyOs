import pc
import os

def safescan(filen):
    with open(filen, encoding="utf8") as file_in:
        drcheck = ""
        for line in file_in:
            drcheck = drcheck + line
        drcheck = drcheck.lower()
        drcheck = drcheck.strip()
        oscheck = "os.remove"
        oscheckforsneakybypassesbydumbpeople = "importosas"
        if 'fernet' in drcheck or 'shutil.rmtree()' in drcheck or oscheck in drcheck or oscheckforsneakybypassesbydumbpeople in drcheck or "open(" in drcheck:
            print(pc.RED+"WARNING\nTHIS FILE APPEARS TO BE MALICIOUS\nIF YOU DO NOT TRUST THIS FILE\nSHUTDOWN YOUR SYSTEM")
            cont = input(pc.GREY+"\n\n\nContinue to file? (y/n)")
            if cont.lower == "y":
              return
