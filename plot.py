from matplotlib import pyplot
import pickle

data = pickle.load(open("data", "rb"))

co2 = data[0]
humid = data[1]
temp = data[2]
dates = data[3]
pyplot.plot_date(dates, co2, 'b-')
pyplot.plot_date(dates, humid, 'g-')
pyplot.plot_date(dates, temp, 'r-')

pyplot.show()