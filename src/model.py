from joblib import load, dump
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from .top_news_selector import TopNewSelector
from .text_preprocessor import hausa_text_preprocessor
from pathlib import Path
from .utils import get_data
import os


class Model:
    def __init__(self, model_path: str = None):
        self._model_path = model_path
        self._model = None
        self.load()

    def train(self, X: list, y=None):
        self._model = Pipeline([('tf_idf', TfidfVectorizer(use_idf=True, preprocessor=hausa_text_preprocessor,
                                                           ngram_range=(1, 2))),
                                ('top_news_selector', TopNewSelector(top_n=3))])
        self._model.fit(X)
        return self

    def predict(self, X: list, word_length: int):
        top_news_ix = self._model.transform(X)
        return [X[ix][:word_length] for ix in top_news_ix]

    def load(self):
        try:
            self._model = load(self._model_path)
        except FileNotFoundError:
            pass
        return self

    def save(self):
        if self._model is not None:
            dump(self._model, self._model_path)
        else:
            raise TypeError(
                'Model not saved yet please train model with .train and try again')

    def __repr__(self):
        return f'model path:{self._model_path}, model:{self._model}'


model_path = Path(__file__).parent / '../model/model.joblib'
model = Model(model_path)


def get_model():
    return model


if __name__ == "__main__":
    data = get_data()
    model.train(data)
    model.save()
