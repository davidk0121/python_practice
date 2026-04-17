# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variable
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()