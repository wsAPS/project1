#!/usr/bin/env python


import os
import sys
import platform
import subprocess
from time import sleep
sys.path.insert(0,"Setup")
import APS2_lib
sys.dont_write_bytecode = True


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main_starting():
	iw = True
	while iw:
		APS2_lib.banner()
		APS2_lib.python_version_cheker()
		APS2_lib.menu()
		ans = raw_input("\n[>] Please insert choice\'s number: "+bcolors.OCRA+bcolors.BOLD)
		print(bcolors.ENDC+'\n')
		if ans == "1":
			print("No make this menu")
			sleep(0.10)
		elif ans == "2":
			print("Plese wait update")
			sleep(0.10)
		elif ans == "3":
			print("HI")
			sleep(0.10)
		elif ans == "4":
			print("No make this menu")
			sleep(0.10)
		elif ans == "5":
			print("Plese wait update")
			sleep(0.10)
		elif ans == "6":
			print("HI")
			sleep(0.10)
		elif ans == "7":
			print("No make this menu")
			sleep(0.10)
		elif ans == "8":
			APS2_lib.msf_handler()
			sleep(0.10)
		elif ans == "9":
			print(bcolors.RED + bcolors.BOLD+"Plese waiting for open website.....")
			cmd0=os.system("firefox aps.or.kr")
			sleep(0.10)
		elif ans == "0":
			APS2_lib.clear()
			print(bcolors.RED + "\n[<< A P S --EXIT>>]\n\n" + bcolors.ENDC)
			sleep(0.2)
			APS2_lib.exit_banner()
			sleep(0.2)
			quit()
	

if __name__ == "__main__":
	main_starting()
	
