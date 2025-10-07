import requests
from bs4 import BeautifulSoup

def zastepstwa_get():
    url = "https://zastepstwa.zse.bydgoszcz.pl"
    strona = requests.get(url)
    return strona

def str_cleanup(x: str):
    x = x.replace('[', '').replace(']', '')
    x = x.replace('<td>', '').replace('</td>', '')
    x = x.replace('<tr>', '').replace('</tr>', '')
    x = x.replace('<tr>', '').replace('</tr>', '')
    ch = 0
    check = 0
    while ch < len(x):
        temp = 0
        if x[ch] == '<':
            check = 1
        elif x[ch] == '>':  
            check = 0
        if check == 1:    
            temp += 1
        x = x[:ch] + x[ch + temp:]    
        ch += 1    
        print(x)

    return x


def main():
    html = zastepstwa_get()
    soup = BeautifulSoup(html.content.decode('iso-8859-2'), 'html.parser')
    zastepstwa = soup.select("table")
    strzastep = str(zastepstwa)
    strzastep = str_cleanup(strzastep)
    print(strzastep)

    with open('test.txt', 'w') as f:
        f.write(strzastep)


main()