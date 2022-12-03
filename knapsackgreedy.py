import numpy

knapsackWeight = 25
currentWeight = 0

value = [100,120,60]
weight = [10,30,20]

totalValue = 0
valueGained = []
valueDensity = []
x = [] # Fractional Quantity or Whole ( 0 to 1)

for i in range(len(value)):
    vd = value[i]/weight[i]
    valueDensity.append(vd)

valueDensityNumpy = numpy.array(valueDensity)

sort_index = list(numpy.argsort(valueDensityNumpy)[::-1])

print("Sort Index = ", sort_index)
print("Value Density = ", valueDensity)

for i in range(len(value)):
    if(currentWeight < knapsackWeight):
        if currentWeight + weight[sort_index[i]] <= knapsackWeight:
            currentWeight += weight[sort_index[i]]
            x.append(1)
            valueGained.append(value[sort_index[i]])
        else:
            rem = (knapsackWeight - currentWeight)/ weight[sort_index[i]]
            x.append( rem )
            currentWeight = knapsackWeight
            valueGained.append(rem*value[sort_index[i]])
    else:
        valueGained.append(0)
        x.append(0)

for i in range(len(valueGained)):
    totalValue += valueGained[i]

print("Value Gained = ", valueGained)
print("Printing X - ", x)

print("Total Value = ", totalValue)
