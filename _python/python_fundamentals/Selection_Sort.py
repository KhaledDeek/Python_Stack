
arr = [8,5,2,6,9,3,1,4,8,7]
def sort(arr):
    newArray = []
    for i in range(len(arr)):
        x = min(arr) 
        newArray.append(x)
        arr.remove(x)
    print(newArray)

sort(arr)

