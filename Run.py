
# ---------------- Imports
import os
import shutil

try:
    import pyzipper
    import colorama
    from rich import print
    from rich.panel import Panel
    import re
except ImportError:
    _ = os.system('pip install colorama' if os.name == 'nt' else 'pip3 install colorama')
    _ = os.system('pip install pyzipper' if os.name == 'nt' else 'pip3 install pyzipper')
    _ = os.system('pip install rich' if os.name == 'nt' else 'pip3 install rich')

import pyzipper
import sys
from time import sleep
from getpass import getpass
from colorama import Fore
from rich.panel import Panel
import os

# -------------------Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
gr = "\033[0;90m"

y = r
os.system("clear")
# ------------------banners
logo = Panel(""" [bold green]
\t</> Developer : STARK-404 </>
\t</> Github : STARK-404 </>
\t</> INSTA : la1uuuuu </>
""",width=50,style="bold hot_pink2",title='(Wp-venom)')

def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def exixting_directory_file(file):
    if os.path.exists(file):
        os.system("node index.js")

def designprint(samaywrite):
    print(logo)
    print(R+"└─> "+d+g+samaywrite)
    print("[bold green]Please Wait Files Are Extracting ...")

def front_design():
    cls_clear_func()
    banner()

front_design()


class Setup:
    def __init__(self,user):
        self.data = user
    def mainFile(self):
        self.save = self.data
        try:
            with pyzipper.AESZipFile('venom.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.extractall(pwd=str.encode(self.save))
            designprint(f'{g}Password Correct !')
            sleep(2.3)
            front_design()
            designprint(f'{g}Extraction Sucessfull..✓')
            sleep(3.0)
            exixting_directory_file('venom.zip')
            os.system('node index.js' if os.name=='nt' else 'node index.js')
        except Exception as samay:
            designprint(f'{r}Password Incorrect !')
            print(f"{gr}[{r}!{gr}]{r}Contact Admin For Password!")
            os.system("xdg-open mailto:unknownshooter509@gmail.com?Subject='Lock!'&Body='I`m%20to%20Buy!")
            os.system('python Run.py' if os.name=='nt' else 'python3 Run.py')


try:
    user_ezip_unzipping = getpass(r+"[ "+g+"× "+r+"]" +g+"Enter password For Decrypt the Zip " +r+">"  ).strip()
except:
    pass

if __name__ == '__main__':
    exixting_directory_file('node index.js')
    main_start = Setup(user_ezip_unzipping)
    main_start.mainFile()





