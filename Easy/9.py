class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if [y for y in str(x)] == [y for y in str(x)][::-1]:
            return True
        else:
            return False