from matplotlib import pyplot
import pickle

data = pickle.load(open("data", "rb"))

pyplot.plot(data)
pyplot.show()