
import unittest

def reverseList(lst):
    for i in range(int(len(lst)/2)):
        lst[i] , lst[len(lst)-1-i] = lst[len(lst)-1-i] , lst[i]
    return lst

1#
class ReverseTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    
    def testTwo(self):
        self.assertEqual(reverseList([1,2,3,4,5]), [5,4,3,2,1])

    def testThree(self):
        self.assertEqual(reverseList([1,2,3,4,5,6,7]), [7,6,5,4,3,2,1])

    def testFour(self):
        self.assertEqual(reverseList([1,2,3,4,5,6,7,8,9]), [9,8,7,6,5,4,3,2,1])

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")

2#

def isPalindrome(txt):
    name = str(txt)[::-1]
    if name == txt : 
        return True



class is_PalindromeTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isPalindrome("racecar") , True)

    def testTwo(self):
        self.assertEqual(isPalindrome("khaled") , True)
    
    def testThree(self):
        self.assertEqual(isPalindrome("rar") , True)

    def testFour(self):
        self.assertEqual(isPalindrome("ahmad") , True)

    def testFive(self):
        self.assertEqual(isPalindrome("dad") , True)

    def testFive(self):
        self.assertEqual(isPalindrome("mom") , True)

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")


3#
def coin(amount):
    coins = [0,0,0,0]
    quarter = 25 
    dime = 10 
    nickel = 5 
    pinnis = 1 
    for i in range(amount):
        if amount >= 25 :
            coins[0] +=1
            amount = amount -25
        elif amount >=10 <25 :
            coins[1] += 1 
            amount = amount -10
        elif amount >=5 <10 :
            coins[2] += 1 
            amount = amount -5
        elif amount >=1 <5 :
            coins[3] += 1 
            amount = amount -1
    return coins

class coinTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coin(87) , [3,1,0,2])

    def testTwo(self):
        self.assertEqual(coin(105) , [4,0,1,0])
    
    def testThree(self):
        self.assertEqual(coin(207) , [8,0,1,2])

    def testFour(self):
        self.assertEqual(coin(156) , [6,0,1,1])

    def testFive(self):
        self.assertEqual(coin(452) , [18,0,0,2])

    def testFive(self):
        self.assertEqual(coin(54) , [2,0,0,4])

    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")



4#
def factorial(num):
    factor = 1
    for i in range(num , 0 , -1 ):
        factor = factor*i
    return factor
    
class factorialTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5) , 120)

    def testTwo(self):
        self.assertEqual(factorial(4) , 24)
    
    def testThree(self):
        self.assertEqual(factorial(9) , 362880)

    def testFour(self):
        self.assertEqual(factorial(3) , 6)


    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")

5#

def fib(num):
    fibbonacci = [0 , 1]
    for i in range(num-1):
        sum = fibbonacci[i] + fibbonacci[i+1]
        fibbonacci.append(sum)
    return fibbonacci[num] 

class fibbonacciTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fib(5) , 5)

    def testTwo(self):
        self.assertEqual(fib(4) , 3)
    
    def testThree(self):
        self.assertEqual(fib(6) , 8)

    def testFour(self):
        self.assertEqual(fib(7) , 13)


    def setUp(self):

        print("running setUp")

    def tearDown(self):

        print("running tearDown tasks")



if __name__ == '__main__':
    unittest.main() 


