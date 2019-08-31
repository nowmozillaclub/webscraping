import bs4
import requests

res = requests.get('https://www.billboard.com/charts/hot-100')
soup = bs4.BeautifulSoup(res.text, 'lxml')

songs = soup.select('span.chart-list-item__title-text')
artists = soup.select('div.chart-list-item__artist')

for i in range(len(songs)):
    print(f'#{i+1}: {songs[i].text.strip()} by {artists[i].text.strip()}\n')
