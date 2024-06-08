import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self,num, *nums):
        self.result = self.result
        for i in range(0,len(nums)):
            self.result+= nums[i]
        self.result += num
        return self.result
    def subtract(self, num, *nums):
        for i in range(0,len(nums)):
            self.result-= nums[i]
        self.result -= num
        return self.result




class MathDojoTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(self.md.add(2,4,6) , 12)
    
    def testTwo(self):
        self.assertEqual(self.md2.add(2,5,7), 14)

    def testThree(self):
        self.assertEqual(self.md3.add(7,2,4,6), 19)

    def setUp(self):
        self.md = MathDojo()
        self.md2 = MathDojo()
        self.md3 = MathDojo()
        print("\nRunning setUp method...")
        
    def tearDown(self):
        print("Running tearDown method...")





if __name__ == '__main__':
    unittest.main() 



