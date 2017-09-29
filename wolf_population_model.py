#!/usr/bin/env python
# from modsim import *
import numpy as np
import pandas as pd
import matplotlib as plt
import pylab


def historical_data_set(data_set = "data/wolf_data_set.csv", index_col="Year"):
	"""
	Creates a plot of the csv file passed to the function with the given index
	column as well. Defaults to the wolf data with time indexing.

	data_set : The path to the csv file needed
	index_col : The column from which to index the data.
	"""
	data = pd.read_csv(data_set, index_col=index_col)	
	return data

def kill_wolves(base_plot,starting_amount=139, starting_year=1915, ending_year=1922):
	"""
	Simulates wolf hunting in yellowstone based on historical data.
	"""
	period = np.arange(starting_year, ending_year, .01)
	values = starting_amount - (period - ending_year + 20) ** 2 + 170
	graph = pd.DataFrame(values, period)
	return graph


def reintroduce_wolves(base_plot, starting_amount = 139, starting_year = 1995, ending_year=2025):
	"""
	Reintroduces wolves to population.
	"""
	# tune the growth rate or multiplier to tune the model.
	growth_rate = 40
	multiplier = .1
	period = np.arange(starting_year, ending_year , .01)
	values = starting_amount+growth_rate*(np.sin(multiplier*np.pi*period))
	graph = pd.DataFrame(values, period)
	return graph	
	
def get_and_plot_elk_data(base_plot, wolf_graph, starting_year = 139, ending_year = 2025):
	"""
	"""
	period = np.arange(starting_year, ending_year, .01) 
	values = -3 * (wolf_graph - 142)**2 + 12000
	graph = pd.DataFrame(values, period)
	return graph

def wolf_summary():
	"""
	Summarizes mathematical model of historical data.
	TODO parameterize this, maybe
	"""
	base_plot = historical_data_set()
	wolves_killing_plot = kill_wolves(base_plot)
	wolves_reintroducing_plot = reintroduce_wolves(base_plot)
	fig, ax = plt.pyplot.subplots()
	ax.plot(base_plot, label="Historical data", color="green")
	ax.plot(wolves_killing_plot, label="Wolf hunting prediction")
	ax.plot(wolves_reintroducing_plot, label="Wolf reintroduction prediction")
	ax.set_xlabel("Years")
	ax.set_ylabel("Number of wolves")
	ax.set_ylim([0, 200])
	ax.legend(loc="best")
	ax.set_title("Wolf population data model")
	pylab.show()
 

wolf_summary()
