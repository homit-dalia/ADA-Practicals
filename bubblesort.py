def bubbleSort(array):
  
  for i in range(len(array)):

    for j in range(len(array)- 1):

         if array[j] > array[j + 1]:

            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

data = [4,2,3,7,-2,-4,9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
