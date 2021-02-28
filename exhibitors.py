# List of exhibitors at NeoCon 2021

from bs4 import BeautifulSoup
import requests

url = "https://neocon.com/exhibitors/explore-exhibitors"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

company = soup.find_all('span', {'class': 'exh'})
for name in company:
    print(name.text.strip())

