data = [5,4,3,2,1,88,17,91,41,54,6,14,0]

for i in range (1, len(data)):
    key = data[i]
    j = i -1

    while j >=0 and key < data[j]:
        data[j+1] = data[j]
        j-=1

    data[j+1] = key


print(data)

