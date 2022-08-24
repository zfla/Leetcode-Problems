class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        list = []
        solved = False
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] + nums[y] == target and x != y:
                    list.append(x)
                    list.append(y)
                    solved = True
            if solved == True:
                break
        return list