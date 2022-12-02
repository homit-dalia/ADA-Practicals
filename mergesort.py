def mergeSort(list):
    print("Splitting ",list)
    
    if len(list)>1:
        
        mid = len(list)//2
        leftHalf = list[:mid]
        rightHalf = list[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        i=j=k=0
        
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                list[k]=leftHalf[i]
                i=i+1
            else:
                list[k]=rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf):
            list[k]=leftHalf[i]
            i=i+1
            k=k+1

        while j < len(rightHalf):
            list[k]=rightHalf[j]
            j=j+1
            k=k+1
    print("Merging ",list)

list = [13,21,47,12,18,54,17,19,1,44]

mergeSort(list)
print(list)
