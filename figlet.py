from pyfiglet import Figlet
import sys
import random

f=Figlet()
font_list=f.getFonts()

if len(sys.argv)==1:
    f.setFont(font=random.choice(font_list))
    cfont=f.renderText(input("Input: "))
    print(cfont)

elif len(sys.argv)==3:
    if (sys.argv[1]=="-f" or sys.argv[1]=="--font") and sys.argv[2] in font_list:
        f.setFont(font=sys.argv[2])
        cfont=f.renderText(input("Input: "))
        print(cfont)
    else:
        sys.exit()
else:
    sys.exit()

