import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sl = "SepalLengthCm"
sw = "SepalWidthCm"
pl = "PetalLengthCm"
pw = "PetalWidthCm"

df = pd.read_csv("iris_data.csv")
df1 = df[[sl, sw]]
df2 = df[[sl, pl]]
df3 = df[[sl, pw]]
df4 = df[[sw, pl]]
df5 = df[[sw, pw]]
df6 = df[[pl, pw]]
df_list = [df1, df2, df3, df4, df5, df6]

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)
plots = [ax1, ax2, ax3, ax4, ax5, ax6]
plt.subplots_adjust(wspace=0.4, hspace=0.5)

for i in range(len(df_list)):
    x = df_list[i].columns[0]
    y = df_list[i].columns[1]
    plots[i].scatter(df_list[i][x], df_list[i][y])
    plots[i].set_title(f"{y} on {x}")
    plots[i].set_xlabel(x)
    plots[i].set_ylabel(y)

    slope, intercept = np.polyfit(df_list[i][x], df_list[i][y], 1)
    #  function was suggested by google AI answers
    plots[i].plot(df_list[i][x], slope * df_list[i][x] + intercept)
    print(f"{y} от {x}: slope = {slope}, intersept = {intercept}")

plt.show()
