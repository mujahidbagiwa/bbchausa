
class MockModel:
    def __init__(self):
        self._model = None

    def train(self):
        return self

    def predict(self):
        return ['maganganu na hausawa', 'bbc hausa ke magana', 'muna tare da ku kullum']

    def load(self):
        return self

    def save(self):
        pass
