from random import randint
import urllib
import time

i = 0

def convertStr(s):
    """Convert string to either int or float."""
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


proxies = []
protocols = ["http", "https", "socks4", "socks5"]

# Reading ProxyList

with open('proxies.txt') as openfileobject:
    for line in openfileobject:
        proxies.append(line)


#Output Text
warn = bcolors.OKGREEN + '[!]' + bcolors.ENDC + ' '
error = bcolors.WARNING + '[!]' + bcolors.ENDC + ' '
info = bcolors.HEADER + '[!]' + bcolors.ENDC + ' '
prompt = "(" + bcolors.BOLD + "proxyminy" + bcolors.ENDC + ")" + ' ' + "> " 


print('''

   ___                            _
  / _ \_ __ _____  ___   _  /\\/\\ (_)_ __  _   _ 
 / /_)/ '__/ _ \\ \\/ / | | |/    \\| | '_ \\| | | |
/ ___/| | | (_) >  <| |_| / /\\/\\ \\ | | | | |_| |
\\/    |_|  \\___/_/\\_\\__,  \\/    \\/_|_| |_|\\__, |
                     |___/                |___/ 
                                            
''')

print(info + " " + str(len(proxies)) + " Proxy Loaded from list. \n")

try:
    #Inputs 
    destination = raw_input(prompt + "Url to Mine : ")
    
    repeat = True
    while repeat :  
        REQUESTS = raw_input(prompt + "How many requests ? ")
        if REQUESTS.isdigit(): 
           repeat = False
           val = convertStr(REQUESTS)
    
    
    # Core Script
    while i < val:

        
        choose = randint(0,len(proxies)-1)
        success = False
        
		# For each protocols attempting a request
		
        for protocol in protocols:
            try:
                urllib.urlopen(str(destination), proxies = {protocol : proxies[choose]})
                print (warn + "Loop[" + str(i+1) + "] Successfully Connected (" + protocol + ") with Proxy Number : " + str(choose))
                success = True
        
		# Capturing interrupt to stop the script whenever you want
	    except KeyboardInterrupt:
		print ("")
	        exit()
	    
	    except:
                print (error + "Loop[" + str(i+1) + "] Failed to connect (" + protocol + ") with Proxy Number : " + str(choose))
		pass
			                        
        if success == False:
            print (error + "Loop[" + str(i+1) + "] Failed to connect with Proxy Number : " + str(choose))
        
        i+= 1

#Catching Keyboard Shortcuts
except KeyboardInterrupt:
    print ("")
    exit()
