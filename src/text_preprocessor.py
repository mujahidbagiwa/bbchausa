import re


def hausa_text_preprocessor(text):

    text = text.lower()
    text = re.sub('\\W', ' ', text)

    words = text.split(' ')
    words = [re.sub('(.*)wa$', '\\1', word) for word in words]
    words = [re.sub('[0-9]', '', word) for word in words]
    return ' '.join(words)
