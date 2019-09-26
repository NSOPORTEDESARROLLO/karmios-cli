#!/usr/bin/python3

import sys
import locale
from dialog import Dialog



opt=[("1","Install New NSID"),("2","Uninstall NSID"),("3","Check NSID Conectivity")]


#This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
d.add_persistent_args(["--backtitle", "KarmiOS-CLI Admin Center"])
d.add_persistent_args(["--title", "NSID Settings"])
d.add_persistent_args(["--clear"])
d.add_persistent_args(["--cancel-label","Return"])


opt = code , tag = d.menu("Please Select an Option:", choices=opt )

#Me devuelvo 
if str(opt[0]) == "cancel":
	sys.path.append('/opt/karmios-cli/bin')
	import karmios_control_center_gui


if opt[1] == "1":
	import new_nsid_gui

elif opt[1] == "2":
	import del_nsid_gui

elif opt[1] == "3":
	import check_nsid_gui


