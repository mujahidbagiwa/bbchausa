from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from preparation import prepare_data
from top_news_selector import TopNewSelector
from text_preprocessor import hausa_text_preprocessor
from preparation import prepare_data
from joblib import load, dump
from utils import get_data
import sys
import click


class RecommendationModel:

    def __init__(self, model_path=None):
        try:
            self.model = load(model_path)
        except FileNotFoundError as fnf:
            print(
                'Invalid path provided, check and update path to point to model location')
            raise
        except TypeError as te:
            print('No model provided please train and model first')

    def train_model(self, train_data, model_path: str):
        train_pipeline = Pipeline([('tf_idf', TfidfVectorizer(use_idf=True, preprocessor=hausa_text_preprocessor,
                                                              ngram_range=(1, 2)))])
        train_pipeline.fit_transform(train_data)
        print(
            f'fitting pipeline consisting of {steps[0] for steps in train_pipeline.steps}')

        self.model = train_pipeline
        dump(train_pipeline, model_path)
        print(f'model trained and saved to {model_path}')

    def predict(self, predict_data_path: str, predict_data=None):
        predict_pipeline = Pipeline([('model', self.model),
                                     ('top_news_selector', TopNewSelector())])

        if predict_data == None:
            if predict_data_path:
                predict_data = get_data(predict_data_path)

        top_news_ix = predict_pipeline.transform(predict_data)

        return [predict_data[index][:200] for index in top_news_ix]
