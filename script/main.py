import requests
from json import loads
from bs4 import BeautifulSoup


def reader(url: str) -> BeautifulSoup:
    response = requests.get(url)
    assert response.status_code == 200
    return BeautifulSoup(response.text, 'html.parser')


def parser(soup: BeautifulSoup) -> str:
    try:
        script = loads(soup.find('script', {'id': '__NEXT_DATA__'}).get_text())
        return script['props']['pageProps']['liveDetailProp']['playAddr']['ori_m3u8']
    except TypeError:
        return 'N/A'


if __name__ == '__main__':
    print(parser(reader('https://www.idevkit.com/live/1069')))
