from pathlib import Path


def get_data(path=Path(__file__).parent / '../data/raw/hausa_news.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(f'Collecting data from {path}')

    return data
