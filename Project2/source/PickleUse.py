import pickle

def pickle():
    json = { 'name': 'rahul', 'age':22}
    t = pickle.dumps(json)
    print(t)

pickle()