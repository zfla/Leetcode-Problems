class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        negative = False
        string = str(x)
        if string[0] == "-":
            negative = True
            string = string.replace("-","")
            
        string = string[::-1]
        
        if negative:
            string = "-" + string
        
        num = int(string)
        
        if num <= -2**31 or num >= 2**31 - 1:
            return 0
        
        return num
        