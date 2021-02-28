from bs4 import BeautifulSoup
import requests

url = "https://www.advfn.com/nasdaq/nasdaq.asp?companies=A"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

company = soup.find_all('span', {'class': 'exh'})
for name in company:
    print(name.text.strip())

