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
