from bs4 import BeautifulSoup
from requests import get


extensions = ('.jpg', '.jpeg', '.png')


def lovely_soup(u):
    h = {'User-Agent': 'Chrome'}
    r = get(u, headers=h)
    c = r.text
    return BeautifulSoup(c, 'lxml')


def get_img(get_url):
    if get_url.endswith(extensions):
        img_name = 'images/{}'.format(get_url.split('/')[-1])
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
