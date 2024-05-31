
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





if __name__ == '__main__':
    unittest.main() 


