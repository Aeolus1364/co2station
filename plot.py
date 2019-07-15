from matplotlib import pyplot
import pickle

data = pickle.load(open("data1", "rb"))

pyplot.plot(data[0])
# pyplot.plot(data1[1])
pyplot.show()