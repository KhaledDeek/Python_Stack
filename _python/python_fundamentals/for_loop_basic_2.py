1#.
numlist = []
def biggie_size(x):
    for i in range(0,len(x)):
        if x[i] > 0 : 
            numlist.append("big")
        else: 
            numlist.append(x[i])
    print(numlist)

biggie_size([-1, 3, 5, -5])



2#.
def count_positives(x):
    count = 0
    for i in range(0,len(x)):
        if x[i]> 0: 
            count += 1
    x[len(x)-1] = count
    print(x)

count_positives([1,6,-4,-2,-7,-2])


3#.
def  sum_total(x):
    count = 0 
    for i in range(len(x)):
        count += x[i]
    print(count)

sum_total([1,2,3,4])



4#.
def average(x):
    count = 0
    for i in range(len(x)):
        count += x[i]
    avg = count/len(x)
    print(avg)

average([1,2,3,4])

5#.
def length(x):
    print(len(x))

length([37,2,1,-9])
length([])


6#.
def minimum(x):
    print(min(x))

minimum([37,2,1,-9])


7#.
def maximum(x):
    print(max(x))

maximum([37,2,1,-9])

8#.
def  ultimate_analysis(x):
    for i in range(len(x)):
        dictionary = {'sumtotal': x[0] ,'average':   x[1]      , 'minimum':     x[2]   , 'maximum':  x[3] , 'length': len(x)  }
    print(dictionary)

ultimate_analysis([37,2,1,-9])


9#.
def reverse_list(x):
    x.reverse()
    print(x)

reverse_list([37,2,1,-9])