class Underscore:
    def map(self ,arr, callback):
        x=[]
        for i in range(len(arr)):
            x.append(callback(arr[i]))
        print(x)
    def find(self ,arr, callback):
        for i in range(len(arr)):
            if callback(arr[i]) == True :
                print(arr[i])
                break
    def filter(self ,arr, callback):
        x = []
        for i in range(len(arr)):
            if callback(arr[i]) == True:
                x.append(arr[i])
        print(x)
    def reject(self ,arr, callback):
        x = []
        for i in range(len(arr)):
            if callback(arr[i]) == False:
                x.append(arr[i])
        print(x)



_ = Underscore() 
_.map([1,2,3],lambda x:x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]


