import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
data.plot(kind ="scatter", x='year', y='selling_price')
plt.grid()
plt.show()