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
Radius = []

for d in starData:
    starName.append(d[1])
    Radius.append(d[4])

w = 0.5
plt.bar(starName, Radius, w)
plt.xlabel('Star Name')
plt.ylabel('Star Radius')
plt.show()