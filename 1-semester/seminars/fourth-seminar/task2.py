import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1337)

number = [10, 100, 1000, 10000]
fig = plt.figure(figsize = (16,16))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
plots = [ax1, ax2, ax3, ax4]
plt.subplots_adjust(wspace=0.4, hspace=0.5)

for i in range(len(number)):
    samples = rng.normal(size=number[i])
    plots[i].hist(samples, bins = 75)
    plots[i].set_title(f"n = {number[i]}")
    plots[i].set_xlabel("Objects")
    plots[i].set_ylabel("Values")

plt.show()
