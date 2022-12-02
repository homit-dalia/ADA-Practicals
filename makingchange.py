denomination = [1, 2, 5, 10, 20]
amountToBePaid = 17
table = []

for i in range(len(denomination) + 1):
    row = []
    for j in range(amountToBePaid + 1):
        row.append(0)        
    table.append(row)
    
for i in range(len(denomination) + 1):
    row = []
    if i >= 1:
        coin = denomination[i-1]
    for j in range(amountToBePaid + 1):
        if i == 0:
            value = 999999
        elif j == 0:
            value = 0
        elif j < coin:
            value =table[i-1][j]
        else:
            v1 = table[i-1][j]
            v2 = 1 + table[i][j - coin]
            value = min(v1, v2)
        table[i][j] = value


for i in range(len(table)):
    print(table[i])
