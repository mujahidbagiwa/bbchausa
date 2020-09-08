def get_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(f'Collecting data from {path}')

    return data
