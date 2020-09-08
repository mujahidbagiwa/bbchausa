import re

from urllib.request import urlopen
from bs4 import BeautifulSoup


def retrieve_new_data(url: str) -> str:
    html_data = urlopen(url).read().decode('utf-8')
    return html_data
