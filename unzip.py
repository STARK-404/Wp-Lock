import os
import zipfile
import time
import rich
from colorama import Fore
from rich.panel import Panel
from rich import print
#colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
def clr_lgtv ():
	os.system('cls' if os.name=='nt' else 'clear')
	
	
logo = Panel(""" [bold green]
\t</> Developer : STARK-404 </>
\t</> Github : STARK-404 </>
\t</> INSTA : la1uuuuu </>
""",width=50,style="bold hot_pink2",title='(Wp-venom)')
if os.path.exists('index.js'):
	os.system("node index.js")
else:
	pass


def unzip_file(zip_file, password=None):

    zip_file = os.path.abspath(zip_file)
    dest_dir = os.path.dirname(zip_file)

    try:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            if password:
                zf.setpassword(password.encode())
            zf.extractall(dest_dir)
        print("[bold green]Extraction Sucessfull..✓")
        time.sleep(0.5)
        os.system('node  /main/index.js')

    except zipfile.BadZipfile:
        print("Zip File Error")
    except RuntimeError:
        print(f"[bold white][[bold red] •[bold white] ][bold red]Incorrect password. Please try again.")
        
        time.sleep(7)
        os.system("xdg-open mailto:unknownshooter509@gmail.com?Subject='Lock!'&Body='I`m%20to%20Buy!'")
        clr_lgtv()
        print(logo)
        password = input(f"{r}[ {g}× {r}] {g}Enter password For Decrypt the Zip {r}>  ")
        unzip_file(zip_file, password)

zip_file = "red.zip"
clr_lgtv()
print(logo)
password = input(f"{r}[ {g}× {r}] {g}Enter password For Decrypt the Zip {r}>  ")
unzip_file(zip_file, password)