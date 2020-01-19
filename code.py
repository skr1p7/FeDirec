import requests
from bs4 import BeautifulSoup


def main():
    index_url = raw_input("Enter index url> ")
    req =requests.get(index_url)
    soup = BeautifulSoup(req.content)
    links = {}
    i = 0
    for a in soup.find_all('a', href=True):
        t = a['href']
        if t.startswith("/"):
           s = t.rfind('/')
           links[i] = t[:s]
           i += 1
        if t.startswith(index_url):
           link = t[len(index_url):]	
           index = link.rfind('/')
           links[i] = link[:index]
           i += 1


    link_list = list(links.values())
    link_list = list(dict.fromkeys(link_list))

    print('Directories on website '+ index_url)

    for x in link_list:
        print (x)
main() 
