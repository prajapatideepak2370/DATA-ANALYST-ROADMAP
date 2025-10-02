import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [1,2,4,5,6]
y = [34,65,23,54, 12]

df = pd.DataFrame({'x': x, 'y': y})


sns.lineplot(data = df, x='x', y='y')
# plt.show()
