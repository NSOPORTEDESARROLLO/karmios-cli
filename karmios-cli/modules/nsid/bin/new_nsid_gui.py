#!/usr/bin/python3

import sys
import locale
from dialog import Dialog

opt = []

#This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
d.add_persistent_args(["--backtitle", "KarmiOS-CLI Admin Center"])
d.add_persistent_args(["--title", "NSID Settings"])
d.add_persistent_args(["--clear"])
d.add_persistent_args(["--cancel-label","Return"])


UserName = code , tag = d.inputbox("Please Insert User:" )

print(UserName)