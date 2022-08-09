import os, sys

os.system ('clear')

logo = ('''
    ______                            __ 
   / ____/___  ____________  ______  / /_
  / __/ / __ \/ ___/ ___/ / / / __ \/ __/
 / /___/ / / / /__/ /  / /_/ / /_/ / /_  
/_____/_/ /_/\___/_/   \__, / .___/\__/  
                      /____/_/             
                      
[1] Encrypt base16
[2] Encrypt base32
[3] Encrypt base64
[4] Encrypt Marshal 
[5] Encrypt Marshal-zlib-base16
[6] Encrypt Marshal-zlib-base32
[7] Encrypt Marshal-zlib-base64
[0] log out ( keluar )
''')

def menu():
    print(logo)
    a = input('\n(+) choose : ')
    if a == '':
        print('\n(+) ngetik apaan lu goblok !!!')
        sys.exit()
    elif a == '1' or a == '01':
        print('ex : /sdcard/file.py')
        os.system('python a')
    elif a == '2' or a == '02':
        print('ex : /sdcard/file.py')
        os.system('python b')
    elif a == '3' or a == '03':
        print('ex : /sdcard/file.py')
        os.system('python c')
    elif a == '4' or a == '04':
        print('ex : /sdcard/file.py')
        os.system('python d')
    elif a == '5' or a == '05':
        print('ex : /sdcard/file.py')
        os.system('python e')
    elif a == '6' or a == '06':
        print('ex : /sdcard/file.py')
        os.system('python f')
    elif a == '7' or a == '07':
        print('ex : /sdcard/file.py')
        os.system('python g')
    else:
    	sys.exit()
        


menu()