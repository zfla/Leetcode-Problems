class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """        
        i = 0
        for j in zip(*strs):
            if len(set(j)) > 1: 
                break
            i+=1
            
        return strs[0][:i]