import re
# import numpy as np

def regEx(dane):
    a = b = c = 'temptext'
    if re.search("W dniu [0-9]+.[0-9]+.[0-9]+ nie zaplanowano zastępstw.", dane[0]):
        a = 0 #"Na jutrzejszy dzień nie zaplanowano żadnych zastępstw"
    x = 1
    while len(dane) > x:    
        if re.search("W .{5,} [0-9]+.[0-9]+.[0-9]+ r. obowiązuje skrócony plan zajęć.", dane[x]):
            b = 1 #"Jutro obowiązuje skrócony plan zajęć."
        if re.search("Dzień wolny od zajęć dydaktycznych", dane[x]):
            c = 1 #"Jutro obowiązuje skrócony plan zajęć."
        x += 1
    if a == 'temptext': a = 1
    if b == 'temptext': b = 0
    if c == 'temptext': c = 0
    
    return a, b, c

def main(): 
    dane = []
    with open('../common/zastepstwa.txt', 'r') as f:
        dane = f.read()
    dane = dane.replace('([\'', '').replace('\'])', '')
    dane = dane.split('], [')
    dane = [item.split('\', \'') for item in dane]
    x = 0
    y = 0
    while x < len(dane):
        while y < len(dane[x]):
            dane[x][y] = dane[x][y].replace('\'', '')
            y += 1
        x += 1
        y = 0
    print(dane)
    print(regEx(dane[0]))

main()