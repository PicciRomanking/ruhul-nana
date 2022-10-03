import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
version="2.2.9"
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
logo=red+str("""
     8888888b.                                          
     888   Y88b                                         
     888    888                                         
     888   d88P .d88b.  88888b.d88b.   8888b.  88888b.  
     8888888P" d88""88b 888 "888 "88b     "88b 888 "88b 
     888 T88b  888  888 888  888  888 .d888888 888  888 
     888  T88b Y88..88P 888  888  888 888  888 888  888 
     888   T88b "Y88P"  888  888  888 "Y888888 888  888""")
     
slogan2="                   ★★★ ℕ𝕒𝕟𝕒 ℕ𝕒𝕥𝕚 𝔾𝕒𝕟𝕘𝕤𝕥𝕖𝕣 ★★★                      "
header=logo+cyan+"\n\n\n\t\tDeveloped By : Picci Roman king\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end

print_check=requests.get("https://pastebin.com/raw/8iYF39Zc").text

if print_check=="header":
	print(header)
elif print_check=="logo":
	print(logo)
elif print_check=="slogan2":
	print(slogan2)