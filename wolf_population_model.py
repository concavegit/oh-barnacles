#!/usr/bin/env python
# Plotting helper functions, just to make life easier.
# from modsim import *
import numpy as np
import pandas as pd
import matplotlib as plt
import pylab

def plot_data_set(data_set = "data/wolf_data_set.csv", index_col="time"):
	"""
	Creates a plot of the csv file passed to the function with the given index
	column as well. Defaults to the wolf data with time indexing.

	data_set : The path to the csv file needed
	index_col : The column from which to index the data.
	"""
	data = pd.read_csv(data_set, index_col=index_col)	
	data.plot()
	pylab.show()
plot_data_set()
