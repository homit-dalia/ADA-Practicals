knapsackWeight = 11

value = [1,6,18,22,28]
weight = [1,2,5,6,7]
numberOfObjects = len(value)

table = []

for i in range(len(value)+1):
    row = []
    for j in range(knapsackWeight+1):
        row.append(0)        
    table.append(row)

for i in range(1,numberOfObjects):
    for j in range(1,knapsackWeight):
        if(weight[i]>j):
            table[i][j] = table[i-1][j]
        else:
            table[i][j] =  max(table[i-1][j], value[i] + table[i-1][j-weight[i]])
            
for i in range(len(table)):
    print(table[i])
