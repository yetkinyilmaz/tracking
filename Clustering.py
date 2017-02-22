
from sklearn.base import BaseEstimator
from sklearn.cluster import DBSCAN

import Transform as transform


class ClusterDBSCAN(BaseEstimator):
    def __init__(self, eps = 0.02):
        self.eps = eps
        self.min_hits = 3
        self.cls = DBSCAN(eps=self.eps, min_samples=self.min_hits)
    
    def fit(self, X, y):
        X=transform.polar(X)
        #        print X
        self.cls.fit(X,y)

    def predict(self, X):
        X=transform.polar(X)
        #        print X
        return self.cls.fit_predict(X)
