import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
plt.plot(data["selling_price"],"r--")
plt.show()