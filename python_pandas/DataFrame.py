import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.co.kr/search?q=삼성전자")

"""
requests 의 .text와  .content의 차이점 -> 어째든 결과값은 둘다 비슷
r.text is the content of the response in unicode, and r.content is the content of the response in bytes.
"""

soup = BeautifulSoup(req.content, 'lxml')
# soup = BeautifulSoup(req.text, 'html.parser')

res_stat = soup.find(id='resultStats').text
print (res_stat)


# ---------------------------------------
code = '005930'
url = 'http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=' + code

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
td = soup.find('td', {'class':'cmp-table-cell td0101'})
print (td)

name = td.find('span', {'class':'name'}).text
print (name)