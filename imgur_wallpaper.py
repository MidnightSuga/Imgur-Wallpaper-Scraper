from bs4 import BeautifulSoup
from requests import get
import os


extensions = ('.jpg', '.jpeg', '.png')


def test_folder():
    if not os.path.isdir('wallpapers'):
        os.mkdir('wallpapers')


def get_img(get_url):
    test_folder()
    if get_url.endswith(extensions):
        img_name = 'wallpapers/{}'.format(get_url.split('/')[-1])
        img = get(get_url).content
        with open(img_name, 'wb') as f:
            f.write(img)


site = get('https://imgur.com/r/wallpaper/new', headers={'User-Agent': 'Chrome'})
soup = BeautifulSoup(site.text, 'lxml')
try:
    for img in soup.findAll('a', {'class': 'image-list-link'}):
        print(img['href'])
        url = 'https://imgur.com{}'.format(img['href'])
        site = get(url, headers={'User-Agent': 'Chrome'})
        soup = (BeautifulSoup(site.text, 'lxml'))
        pic = soup.find('meta', {'name': 'twitter:image'})
        get_img(pic['content'])
except KeyboardInterrupt:
    exit()
