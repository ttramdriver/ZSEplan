import requests
from bs4 import BeautifulSoup

def zastepstwa_get():
    url = "https://zastepstwa.zse.bydgoszcz.pl"
    strona = requests.get(url)
    return strona

def str_cleanup(x: str):
    x = x.replace('[', '').replace(']', '')
    x = x.replace('<td>', '').replace('</td>', '')
    x = x.replace('<tr>', '/').replace('</tr>', '').replace('</table>', ';')
    x = x.replace('<td align="LEFT" bgcolor="#69AADE" class="st1" colspan="4" nowrap="">', ';')
    x = x.replace('\t', '').replace('\n', '').replace('\r', '')
    ch = 0
    check = 0
    while ch < len(x):
        ch = x.index('>') + 1
        x = x[:x.index('<')] + ', ' + x[x.index('>') + 1:]
    x = x.replace(';', '; \n')
    x = x.replace('/, lekcja, opis, zastępca, uwagi   ', '')
    x = x.replace(',  ,  ,  ,  /', '')
    x = x.replace('/,', '/')
    x = x.replace(' -', ',')
    # print(x)

    return x

def data_process(x: str):
    x = x[x.index('\n') + 1:]
    x = x.replace(' ', '')#.replace(' ', '')
    if len(x) > 0:    
        imiNazw = []
        lekcja = []
        klasa = []
        sala = []
        zastępca = []
        uwagi = []
        i = 0
        start = 0
        end = 0
        elementIndex = 0
        while i < len(x):
            if x[i] == '/':
                if elementIndex == 0:
                    end = i
                    elementIndex = 0
                    imiNazw.append(x[start:end])
                    return imiNazw
            i += 1
                # elif elementIndex == 1:
            # if x[i] == ';':
                # i+=1 
                # elementIndex = -1
        
    # return x

def main():
    html = zastepstwa_get()
    soup = BeautifulSoup(html.content.decode('iso-8859-2'), 'html.parser')
    zastepstwa = soup.select("table")
    strzastep = str(zastepstwa)
    strzastep = str_cleanup(strzastep)
    # print(strzastep)
    
    with open('zastepstwa.txt', 'w') as f:
        f.write(strzastep)
    
    with open('zastepstwa.txt', 'r') as f:
        noInternetZastep = f.read()
    
    with open('test.txt', 'w') as f:
        f.write(str(data_process(noInternetZastep)))
        
       
main()