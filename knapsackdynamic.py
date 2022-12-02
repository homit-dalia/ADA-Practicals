def knapSack(W, weight, value, n):
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build table table[][] in bottom up manner
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i-1] <= j:
                table[i][j] = max(value[i-1] + table[i-1][j-weight[i-1]],  table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    print(table)
    return table[n][W]
    
value = [6,7,8,9,10]
weight = [1,2,3,4,5]
W = 5
n = len(value)

print(knapSack(W, weight, value, n))