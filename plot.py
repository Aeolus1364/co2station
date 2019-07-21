from matplotlib import pyplot
import pickle

data = pickle.load(open("data1", "rb"))

vals = data[0]
dates = data[1]


pyplot.plot_date(dates, vals, 'b-')
# pyplot.plot(data1[1])
pyplot.show()