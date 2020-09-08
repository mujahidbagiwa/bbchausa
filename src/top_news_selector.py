import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class TopNewSelector(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        sum_tfidf = np.array(X.todense().max(axis=1))
        top_n_indices = np.argpartition(sum_tfidf.squeeze(), -3)[-3:]

        return top_n_indices
