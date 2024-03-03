import requests,json,os,sys
os.system("clear")
logo="""

\033[1;36m╔═════════════════════════════════════════╗
•           \033[1;33m<🌺Assalamu Alaikum🌺>        •
\033[1;36m╚════════════════════════════════════════╝
\033[1;32m╔  __  __                 _            
 |  \/  |               | |           
 | \  / | ___  _ __  ___| |_ ___ _ __ 
 | |\/| |/ _ \| '_ \/ __| __/ _ \ '__|
 | |  | | (_) | | | \__ \ ||  __/ |   
 |_|  |_|\___/|_| |_|___/\__\___|_|   
                                      
                                      
════════════════════════════════════════╗
║  \033[1;32m[√] DEVOLPER    :     RaFi    ║
\033[1;32m║  \033[1;33m[√] FACEBOOK    :     RaFi     \033[1;32m║
\033[1;32m║  \033[1;34m[√] WHATAPP     :     01858188295    \033[1;32m ║
\033[1;32m║  \033[1;35m[√] GITHUB      :     Monster-404        \033[1;32m║
\033[1;32m║  \033[1;31m[√] VERSION     :     1.0              \033[1;32m║
\033[1;32m║  \033[1;36m[√] SERVER      :     DATA WORKING    \033[1;32m ║ 
\033[1;32m╚═════════════════════════════════════════╝
"""

print(logo)
#Note=input("This Tool Create By Team Monster ")
victim=input(' \033[1;31mVICTIM IP ADDRESS : ')
url="http://ip-api.com/json/"+victim
ip=requests.get(url).json()

print("""\n
 \033[1;33m--------------------------------------------------
                \033[1;33m VICTIM INFORMATION            
--------------------------------------------------

""")

print(" \033[1;31mVICTIM IP : \033[1;36m "+ip['query'])
print(" \033[1;31mIP STATUS : \033[1;36m "+ip['status'])
print(" \033[1;31mCOUNTRY : \033[1;36m "+ip['country'])
print(" \033[1;31mCOUNTRY CODE : \033[1;36m "+ip['countryCode'])
print(" \033[1;31mDIVISION : \033[1;36m "+ip['regionName'])
print(" \033[1;31mCITY : \033[1;36m "+ip['city'])
#print("DISTRICT : "+ip['district'])
print(" \033[1;31mNETWORK SERVICE : \033[1;36m "+ip['isp'])
print(" \033[1;31mTIMEZONE : \033[1;36m "+ip['timezone'])


  

