import pickle
from mockuser import MockUser2
from source import Calculator2

class PickleUse:

    def pickle(self):
        json = { 'name': 'rahul', 'age':22}
        t = pickle.dumps(json)
        print(t)

pickle()