1#.
for i in range(151):
    print(i)


2#.
for x in range(5,1000):
    if x%5 == 0:
        print(x)
	

3#.
for v in range(1,100):
    if v%10 == 0: print("Coding Dojo")    
    elif v%5 == 0: print("Coding")
    else: 
        print(v)



4#.
sum = 0
for x in range(0,500000):
    if x%2 != 0:
        sum += x
print(sum)    
    


5#.
for c in range(2018,0,-4):
    if c%2 == 0:
        print(c)



6#.
lowNum= 2
highNum = 9
mult = 3

for x in range(lowNum,highNum+1):
    if x%mult == 0:
        print(x)