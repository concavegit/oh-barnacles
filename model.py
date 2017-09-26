import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

palmerAlive = pd.read_csv('data/palmer-alive.csv')
palmerDead = pd.read_csv('data/palmer-dead.csv')
palmerTotal = pd.read_csv('data/palmer-total.csv')
whelks = pd.read_csv('data/whelk_correlation_table.csv')

print(whelks)
