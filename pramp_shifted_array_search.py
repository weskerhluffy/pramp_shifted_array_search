'''
Created on 3 nov 2019

@author: ernestoalvarado
'''
# XXX: https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX
def find_split(arr):
  arr_len = len(arr)
  i = 0
  j = arr_len - 1
  asc = None
  while i < j:
    mid = (i + j) >> 1
    if arr[i] > arr[mid] < arr[j]:
      if arr[i] < arr[j]:
        asc = False
        i = mid
      else:
        asc = True
        j = mid
    else:
      if arr[i] < arr[mid] > arr[j]:
        if arr[i] < arr[j]:
          asc = False
          j = mid
        else:
          asc = True
          i = mid
      else:
        if arr[i]<arr[mid]<arr[j]:
          asc=True
          j=0
          break
        if arr[i]>arr[mid]>arr[j]:
          asc=False
          j=0
          break
        if arr[i] > arr[j]:
          asc = True
        else:
          asc = False
        break
  return j, asc


def bin_search(arr, n, i, j, a):
  arr_len = len(arr)
  while i <= j:
    mid = (i + j) >> 1
    if n > arr[mid]:
      if a:
        i = mid + 1
      else:
        j = mid - 1
    else:
      if n < arr[mid]:
        if a:
          j = mid - 1
        else:
          i = mid + 1
      else:
        return mid
  return -1

      
def shifted_arr_search(shiftArr, num):
  arr_len = len(shiftArr)
  if arr_len<3:
    for i in range(arr_len):
      if shiftArr[i]==num:
          return i     
    return -1
  split_idx, asc = find_split(shiftArr)
  i = None
  j = None
#  print("spl {} asc {}".format(split_idx, asc))
  if not split_idx:
    i = 0
    j = arr_len - 1
  else:
    for k in [0, split_idx - 1, split_idx, arr_len - 1]:
      if num == shiftArr[k]:
        return k      
    if shiftArr[split_idx] < num < shiftArr[arr_len - 1]:
      i = split_idx
      j = arr_len - 1
    if shiftArr[0] < num < shiftArr[split_idx - 1]:
      i = 0
      j = split_idx - 1
    if shiftArr[split_idx] > num > shiftArr[arr_len - 1]:
      i = split_idx
      j = arr_len - 1
    if shiftArr[0] > num > shiftArr[split_idx - 1]:
      i = 0
      j = split_idx - 1
      
  r = bin_search(shiftArr, num, i, j, asc)
  return r

  
tcs = [
  ([9, 12, 17, 2, 4, 5], 2, 3),
  ([2,4,5,9, 12, 17], 2, 0),
  ([17,12,9,5,4,2], 2, 5),
  ([2,4,5,9, 12, 17], 5, 2),
  ([17,12,9,5,4,2], 5, 3),
  ([9, 12, 17, 2, 4, 5], 4, 4),
  ([9, 12, 17, 2, 4, 5], 12, 1),
  ([4,5,9, 12, 17, 2 ], 2, 5),
  ([4,5,9, 12, 17, 2 ], 5, 1),
  ([12,9,5,4,2,17], 17, 5),
  ([12,9,5,4,2,17], 5, 2),
  ([17,2,4,5,9, 12], 17, 0),
  ([17,2,4,5,9, 12], 5, 3),
  ([17,2,4,5,9, 12], 12, 5),
  ([1,2], 1, 0),
  ([1,2], 2, 1),
  ([2,1], 1, 1),
  ([2,1], 2, 0),
]  
for tc, n, er in tcs:
  r = shifted_arr_search(tc, n)
#  print(r)
  assert er == r, "exp {} r {}".format(er, r)
