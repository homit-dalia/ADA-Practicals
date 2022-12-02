def MatChainMul(arr, n):

    matrix = [[0 for i in range(n)] for j in range(n)]
    print(matrix)
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1

            matrix[i][j] = 10**10 #assigning ~ infinite

            for k in range(i, j):
                q = matrix[i][k] + matrix[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if q < matrix[i][j]:
                    matrix[i][j] = q
    
    return matrix[1][n-1]

arr = [30,35,15,5,10,20,25]
size = len(arr)

print("Minimum number of multiplications required are " +str(MatChainMul(arr, size)))
