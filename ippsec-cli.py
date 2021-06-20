from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tabulate import tabulate
from colorama import Fore,init
import sys

webpage = "https://ippsec.rocks/?#"
if len(sys.argv) == 1:
    print("Usage: ippsec-cli <keyword>")
    sys.exit()
searchterm = sys.argv[1]

options = Options()
options.add_argument('--headless')
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(firefox_profile=profile,options=options, service_log_path="/dev/null")
driver.get(webpage)
searchbar = driver.find_element_by_tag_name('input')
searchbar.send_keys(searchterm)
lnks=driver.find_elements_by_tag_name("a")
td=driver.find_elements_by_tag_name("td")
lista = []
ytlink =[]
for i in td:
    lista.append(i.text)
for lnk in lnks:
    youtubelink = lnk.get_attribute("href")
    ytlink.append(youtubelink)

ytlink=ytlink[2:len(ytlink)-5]    
lista =lista[2:len(lista)]
lista = [i.strip() for i in lista]
cleanlist=[]
for x in lista:
    if len(x) > 100:
        x = x[:100]
        cleanlist.append(x)
    else:
        cleanlist.append(x)


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
n = 3
counter=2
for i in ytlink:
    if len(i) >100:
        i = i[:100]
    cleanlist.insert(counter, i)
    counter+=3
final=list(divide_chunks(cleanlist,n))

if len(final) == 0:
    print(Fore.RED+"[-] No results found for search term: "+searchterm)
else:
    headers=["Machine", "Description","Link"]
    init()
    print(Fore.GREEN)
    print(tabulate(final, headers, tablefmt="github"))
    print()
