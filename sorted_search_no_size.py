def elementAt(arr,i):
  if i > len(arr)-1:
    return -1
  else:
    return arr[i]

def binary_search(arr, start, end, target):
  mid = (start+end)//2

  while start <= end:
    if target == elementAt(arr, mid):
      return mid
    if elementAt(arr, mid) == -1:
      return binary_search(arr, start, mid-1, target)
    elif target < elementAt(arr, mid):
      return binary_search(arr, start, mid-1, target)
    else:
      return binary_search(arr, mid+1, end, target)

  return -1

def sorted_search_no_size(arr, target):
"""
  Hooping by multiplication of 2 like 2,4,8,16. If the value is not present in list, 
  then call binary search till that index. Now in binary search the input list is like [1,2,3,None, None, None, None]. 
  If mid == None, call binary search till mid-1. Now, previous mid can never be -1 as the value was being
  mulitpled by 2 at every iteration.
"""
  i = 1
  while elementAt(arr, i) is not -1:
    i = i * 2
  
  return binary_search(arr, 0, i, target)


arr = [1,3,4,5,7,10,14,15,16,19,20,25]
print(sorted_search_no_size(arr, 3))
