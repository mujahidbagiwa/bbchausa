import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class TopNewSelector(BaseEstimator, TransformerMixin):
    def __init__(self, top_n):
        self.top_n = top_n

    def fit(self, X, y=None):
        pass

    def transform(self, X):
        sum_tfidf = np.array(X.todense().max(axis=1))
        top_n_indices = np.argpartition(
            sum_tfidf.squeeze(), -1 * self.top_n)[-1 * self.top_n:]

        return top_n_indices
