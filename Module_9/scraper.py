"""
Program: scraper.py
Author: Dylan Thomas
Last date modified: 10/25/2020
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S'
    response = requests.get(url)
    html = response.content
    f = open("requestResult.txt", "w+")
    f.writelines(str(html))
    f.close()

    soup = BeautifulSoup(open("requestResult.txt"), 'html.parser')
    print(soup.prettify())
