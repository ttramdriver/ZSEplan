import requests
from bs4 import BeautifulSoup

def zastepstwa_get():
    url = "https://zastepstwa.zse.bydgoszcz.pl"
    try:
        return requests.get(url)
    except:
        return 1
    

def str_cleanup(x: str):
    # x = x.replace(';', '.')
    x = x.replace('[', '').replace(']', '')
    x = x.replace('<td>', '').replace('</td>', '')
    x = x.replace('<tr>', '/').replace('</tr>', '').replace('</table>', '!]')
    x = x.replace('<td align="LEFT" bgcolor="#69AADE" class="st1" colspan="4" nowrap="">', '!]')
    x = x.replace('\t', '').replace('\n', '').replace('\r', '')
    ch = 0
    check = 0
    while ch < len(x):
        ch = x.index('>') + 1
        x = x[:x.index('<')] + '| ' + x[x.index('>') + 1:]
    x = x.replace('!]', '!]\n')
    x = x.replace('/| lekcja| opis| zastępca| uwagi   ', '')
    x = x.replace('|  |  |  |  /', '')
    x = x.replace('!]', '|!]').replace('/|!]', '|!]').replace('/|', '/')
    x = x.replace('|  ', '| brak')
    x = x.replace('.| | Rozkład godzinowy dostępny jest pod linkiem: | LINK| | | | |!]', '!]').replace('| |', '|').replace('| / | ', '').replace('.| /  /  |!]', '!]')
    if x[0] == '/' and x[1] == ' ':
        x = x[2:]
    elif x[0] == '/' or x[0] == ' ':
        x = x[1:]
    # print(x)

    return x

def data_sort(x: str):
    tempDaneP = []
    tempDaneP.append(x[0:x.index('!]')])
    tempDaneP = [item.split('| ') for item in tempDaneP]
    daneP = sum(tempDaneP, [])
    if str(daneP[0])[-1] == '|':
        daneP[0] = daneP[0][:-1]
    x = x[x.index('!]') + 3:]
    x = x.replace(' ', '')#.replace(' ', '')
    if len(x) > 0:    
        imiNazw = []
        lekcja = []
        klasa = []
        sala = []
        zastepca = []
        uwagi = []
        i = 0
        start = 0
        end = 0
        elementIndex = 0
        while i < len(x):
            if x[i] == '/':
                end = i
                if elementIndex == 0:   imiNazw.append(x[start:end])
                elif elementIndex == 5: 
                    start += 1
                    uwagi.append(x[start:end])
                elementIndex = 1
                start = i + 1
            elif x[i] == '|':
                start += 1
                end = i
                if elementIndex == 1:   lekcja.append(x[start:end])
                elif elementIndex == 3: sala.append(x[start:end])
                elif elementIndex == 4: zastepca.append(x[start:end])
                elif elementIndex == 5: uwagi.append(x[start:end])
                elementIndex += 1
                start = i + 1
            elif x[i] == '-' and elementIndex == 2:
                end = i - 1
                klasa.append(x[start + 1:end])
                elementIndex += 1
                start = i + 1
            elif x[i] == '!' and x[i+1] == ']':
                lekcja.append(';')
                klasa.append(';')
                sala.append(';')
                zastepca.append(';')
                uwagi.append(';')
                i += 2
                elementIndex = 0
                start = i + 1
            i += 1
        return daneP, imiNazw, lekcja, klasa, sala, zastepca, uwagi
    return daneP
    
def data_process(x: list):
    return 'test'
    
def main():
    # print(zastepstwa_get())
    if zastepstwa_get() != 1:
        html = zastepstwa_get()
        soup = BeautifulSoup(html.content.decode('iso-8859-2'), 'html.parser')
        zastepstwa = soup.select("table")
        strCleanDaneZastepstwa = str_cleanup(str(zastepstwa))
        with open('zastepstwa_raw.txt', 'w') as f:
            f.write(strCleanDaneZastepstwa)
        with open('zastepstwa_sorted.txt', 'w') as f:
            f.write(str(data_sort(strCleanDaneZastepstwa)))
        print(data_process(1))
        # print('no errors')
    else:
        # print('an error occured')
        with open('zastepstwa_raw.txt', 'r') as f:
            noInternetZastepstwa = f.read()

        with open('zastepstwa_sorted.txt', 'w') as f:
            f.write(str(data_sort(noInternetZastepstwa)))
    
    # print(strCleanDaneZastepstwa)
    # with open('zastepstwa_unprocessed saved 1.txt', 'r') as f:
    #     noInternetZastepstwa = f.read()
    
    # with open('zastepstwa saved 1.txt', 'w') as f:
    #     f.write(str(data_sort(noInternetZastepstwa)))
        
       
main()