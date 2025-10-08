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
    x = x.replace('<tr>', '').replace('</tr>', '').replace('</table>', ';')
    x = x.replace('<td align="LEFT" bgcolor="#69AADE" class="st1" colspan="4" nowrap="">', ';')
    x = x.replace('\t', '').replace('\n', '').replace('\r', '')
    ch = 0
    check = 0
    while ch < len(x):
        ch = x.index('>') + 1
        x = x[:x.index('<')] + ', ' + x[x.index('>') + 1:]
    x = x.replace(';', '; \n')
    x = x.replace('lekcja, opis, zastępca, uwagi   , ', '')
    x = x.replace(' -', ',')
    # print(x)

    return x

def get_inf(x: str):
    x = x[x.index('\n') + 1:]
    if len(x) > 0:    
        imiNazw = []
        lekcja = []
        klasa = []
        sala = []
        zastępca = []
        uwagi = []
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