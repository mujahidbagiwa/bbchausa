import sys
import click
from retrieve_data import retrieve_new_data
from bs4 import BeautifulSoup


def prepare_data(url: str, file_name: str, save: bool) -> list:
    html_data = retrieve_new_data(url)
    parsed_data = BeautifulSoup(html_data, 'html.parser')
    prepared_data = parsed_data.get_text().split('.')

    if save:
        with open(f'../data/raw/{file_name}', 'a') as ofile:
            ofile.write('\n'.join(prepared_data))
    return prepared_data
