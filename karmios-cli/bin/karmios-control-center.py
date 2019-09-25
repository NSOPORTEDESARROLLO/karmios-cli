#!/usr/bin/python3

import sys
import locale
from dialog import Dialog
sys.path.append('/opt/karmios-cli/lib')
from modules_info import GetModuleInfo


modules=GetModuleInfo()
opt=[]

for module,description in modules.items():
	opt.append((module,description['description']))




#This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
d.add_persistent_args(["--backtitle", "KarmiOS-CLI Admin Center"])
d.add_persistent_args(["--title", "KarmiOS-CLI"])
d.add_persistent_args(["--clear"])

test = code , tag = d.menu("Please Select an Option:", choices=opt )

print(test[1])