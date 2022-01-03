import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
plt.figure(figsize =(10,3))
x = data["selling_price"]
plt.hist(x,bins=30, color="green")
plt.title("selling_price")
plt.xlabel("km_driven")
plt.ylabel("count")
plt.show()