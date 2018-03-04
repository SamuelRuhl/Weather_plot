# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:11:20 2018

@author: Xram
"""

import urllib.request 
import time

resource = urllib.request.urlopen('https://www.dwd.de/DE/leistungen/_config/leistungsteckbriefPublication.txt?view=nasPublication&nn=16102&imageFilePath=8524108716561010473591414984380285860348440627905136707616031491601294722759953476578874542442119146105183517945099480938740343906988335742522410754862714750285564712567437754031667430876251498672762866772169174718581140918161764870338171972131831101&download=true')

data = resource.readlines()

ti = time.localtime()
f = open("SB_"+str(ti.tm_mday)+"."+str(ti.tm_mon)+"."+str(ti.tm_year)+".txt","w",encoding="utf8")
data = data[5:len(data)-1]
data = list(map(str,data))

arr = []
for line in data:
    midline = len(line)//2
    line = line[2:midline] + line[midline:len(line)-3] + "\n"
    f.write(line)
f.close()
