class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        s = 0
        
        for x in nums:
            s = s + x
            l.append(s)
            
        return l