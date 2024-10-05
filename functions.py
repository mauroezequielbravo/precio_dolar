import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_dolar(url: str, xpath: str):
  req = requests.get(url)
  status_code = req.status_code
  if status_code == 200:
    soup = BeautifulSoup(req.text, 'lxml')

    dom = etree.HTML(str(soup))

    precio = dom.xpath(xpath)
    
    return precio[0].replace('$','')
  else:
    print(status_code)
    return status_code






