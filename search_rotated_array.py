def search_rotated_array(arr, left, right, key):
  mid = int((left+right)/2)

  if key == arr[mid]:
    return mid

  while left <= right:    # if the target is not found, it will return -1
    if arr[left] <= arr[mid]:   # if the left side is normal
      if key < arr[mid] and key >= arr[left]:
        return search_rotated_array(arr, left, mid-1, key)
      else:
        return search_rotated_array(arr, mid+1, right, key)
      
    else:                 # if the right side is normal
      if key > arr[mid] and key <= arr[right]:
        return search_rotated_array(arr, mid+1, right, key)
      else:
        return search_rotated_array(arr, left, mid-1, key)

  return -1

arr = [17, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14, 15, 16]
ar = [10, 14, 15, 16, 17, 19, 20, 25, 1, 3, 4, 5, 7]
arr = [3,1]
key = 1
print (search_rotated_array(arr, 0, len(arr)-1, key))
