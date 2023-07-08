#Note: View the output in fullscreen
import csv
from matplotlib import pyplot as plt

data = []

with open('final.csv', 'r') as f:
    csvrdr = csv.reader(f)
    for x in csvrdr:
        data.append(x)

headers = data[0]
starData = data[1:]

starName = []
Mass = []

for d in starData:
    starName.append(d[1])
    Mass.append(d[3])

w = 0.5
plt.bar(starName, Mass, w)
plt.xlabel('Star Name')
plt.ylabel('Star Mass')
plt.show()