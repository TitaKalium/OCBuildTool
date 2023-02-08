import requests
import zipfile
import os
import platform
import psutil

url = "https://github.com/acidanthera/OpenCorePkg/releases/download/0.8.8/OpenCore-0.8.8-DEBUG.zip"

response = requests.get(url)
open("OpenCore-0.8.8-DEBUG.zip", "wb").write(response.content)

with zipfile.ZipFile("OpenCore-0.8.8-DEBUG.zip", "r") as zip_ref:
    zip_ref.extractall(os.getcwd())
    
os.remove("OpenCore-0.8.8-DEBUG.zip")

os.chdir("Utilities/macrecovery")
subprocess.run(["python3", "macrecovery.py", "-b", "Mac-4B682C642B45593E", "-m", "00000000000000000", "download"])

#Check processor info    
import psutil

cpu_info = psutil.cpu_info()
if 'Intel' in cpu_info.brand:
    if (cpu_info.family >= 6) and (cpu_info.family <= 10):
        print("Intel architecture, generation:", cpu_info.family)
    else:
        print("Computer not supported")
        exit()
    
    if platform.architecture()[0] == '64bit':
        print("64-bit architecture")
    else:
        print("32-bit architecture")
else:
    print("Computer not supported")
    exit()




print("Done")