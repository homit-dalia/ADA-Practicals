def partition(arr, low, high):
    
  pivot=arr[high]
  i=low-1
  
  for j in range(low,high):
    if arr[j]<=pivot:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[high],arr[i+1]=arr[i+1],arr[high]
  return i+1

def quicksort(arr, low, high):
  if low < high:
    part=partition(arr,low,high)
    quicksort(arr,low,part-1)
    quicksort(arr,part+1,high)

arr=[52,14,47,22,17,36]    
quicksort(arr,0,len(arr)-1)
print(arr)
