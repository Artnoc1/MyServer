# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from ux import *
from logo import *

class Un(object):
  def Uni(self):
	while True:
		Mylogo()
		ask = raw_input('''\n\n\033[1;33m Do you want to uninstall MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m''')
		if ask == "n" or ask == "N":
			break
		elif ask == "Y" or ask == "y":
			os.system("rm -rf "+bpath+"myserver && rm -rf ~/.MyServer")
			os.system("cd ~/ && rm -rf MyServer")
			os.system("cd "+spath+" && rm -rf .host.aex .port.aex .path.aex")
			if system=="ubuntu":
			  os.system("cd ~/ && sudo rm -rf MyServer")
			  os.system("sudo rm -rf /usr/bin/myserver && sudo rm -rf ~/.MyServer")
			  os.system("cd "+spath+" && sudo rm -rf .host.aex .port.aex .path.aex")
			exit()
		else:
			print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ask+"\'")
			sleep(1)

Un().Uni()