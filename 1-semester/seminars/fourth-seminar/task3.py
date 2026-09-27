import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('mipt/1-semester/seminars/fourth-seminar/iris_data.csv')
species = df['Species'].value_counts()
print(df)
a = len(df[df["PetalLengthCm"] < 1.2])
b = len(df[(df["PetalLengthCm"] >= 1.2) & (df["PetalLengthCm"] <= 1.5)])
c = len(df[df["PetalLengthCm"] > 1.5])

print(a)
plt.pie(species, labels = species.index)

plt.title('Iris species')

plt.show()

plt.pie([a,b,c,], labels = ['less 1.2 cm', 'between 1.2 cm and 1.5 cm', 'more 1.5 cm'])

plt.title('Iris filter')

plt.show()


