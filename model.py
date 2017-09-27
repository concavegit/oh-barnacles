import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

wolves = pd.read_csv('data/wolf-data.csv').set_index('Year')
