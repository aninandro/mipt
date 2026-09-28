import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


with Path("experiment_data.txt").open() as f:
    content = f.read().splitlines()

content = np.array(content).astype(int)[3600:]

plt.plot(content, label = "Counts registered during 1 second")
plt.ylabel("Number of counts")
plt.xlabel("Time")
plt.title("Obtained values")
plt.legend()
plt.show()
