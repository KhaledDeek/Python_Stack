def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = i
        temp_arr = arr.pop(i)
        for k in range(i-1 , -1 , -1):
            if arr[k]> temp_arr:
                key = k
        arr.insert(key , temp_arr)
    print(arr)

insertion_sort([6,5,3,1,8,7,2,4])