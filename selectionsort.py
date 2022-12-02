list=[44,22,48,47,66,41,8,5,94,39,41,14]

for i in range(len(list)-1):
    minimumElement = list[i]
    for j in range(i+1, len(list)):
        if(list[j] < minimumElement):
            minimumElement = list[j]
            list[j], list[i] = list[i], list[j]
           
print(list)
