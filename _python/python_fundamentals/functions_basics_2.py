1#.
numList = []
def countDown(x):
    for i in range(x, -1, -1):
        numList.append(i)
    print(numList)        


countDown(6)



2#.
def print_and_return(x):
    print(x[0])
    return  x[1]

print(print_and_return([1,2]))



3#.
def FirstPlusLength(x):
    y = len(x)+x[0]
    print(y)

FirstPlusLength([1,2,3,4,5])






4#.
newList = []
def values_greater_than_second(x):
    if len(x) >= 2:
        for i in range(0, len(x), +1):
            if x[i] > x[1]:
                newList.append(x[i])
        print(newList)
        print(len(newList))
    else:
        print("False")

values_greater_than_second([5,2,3,2,1,4]) 





5#.
numlist = []
def length_and_value(a , b):
    for i in range(a):
        numlist.append(b)
    print(numlist)
    


length_and_value(6,2)