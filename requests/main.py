import requests
from bs4 import BeautifulSoup

link ="https://browser-info.ru/"
response = requests.get(link).text
soup = BeautifulSoup(response, "lxml")
block = soup.find('div', id = 'tool_padding')
check_js = block.find('div', id = 'javascript_check')
print(check_js)