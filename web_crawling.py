from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://kosis.kr/covid/covid_index.do")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.find('table'))
