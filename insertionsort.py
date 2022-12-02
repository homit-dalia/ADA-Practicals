def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
               
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
       
        array[j + 1] = key


data = [4,8,6,9,1,2]

#print(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
