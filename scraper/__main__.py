import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging

def main(args=None):
    # fetch from url
    html = urlopen(sys.argv[1])
    product = BeautifulSoup(html.read(), 'html.parser').find(itemtype='http://schema.org/Product')
    own_product = product.find(itemprop="seller", content="eMAG")
    print(product.prettify());

if __name__ == "__main__":
    main()
