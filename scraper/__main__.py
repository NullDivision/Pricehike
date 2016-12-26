import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging

def main(args=None):
    html = urlopen("http://www.emag.ro/placa-video-gigabyte-geforcer-gtx-1070-windforce-oc-8gb-gddr5-256-bit-gv-n1070wf2oc-8gd/pd/DFYJD2BBM/")
    soup = BeautifulSoup(html.read(), 'html.parser')
    print(soup.find_all(itemtype='http://schema.org/Product'));

if __name__ == "__main__":
    main()
