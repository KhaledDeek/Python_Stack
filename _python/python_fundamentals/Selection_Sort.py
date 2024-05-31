def insertion_sort(lst):
    for i in range(len(lst)-1):
        minimum = i 
        for k in range(i+1,len(lst)):
            if lst[k] < lst[minimum]:
                minimum = k
        minimum_value= lst.pop(minimum)
        lst.insert(i,minimum_value)
    print(lst)


insertion_sort([8,5,6,9,3,4,7])