"""
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        i = 0
        while i < len(haystack):
            #First mistake: I don't consider whether hatstack.index(needle[0]) exist
            if needle[0] not in haystack[i:len(haystack)]:
                return -1
                break
            # Fifth mistake: I should update haystack if the one is not substring, so I assign the range of haystack
            possible = i+ haystack[i:len(haystack)].index(needle[0])
            # Second mistake: I don't consider interval upper value possible+len(needle)+1 exceed len(haystack)
            # Second mistake is not mistake, a='123', a[1:6] still makes sense, it is '23'
            
            # Third mistake: I should use : to express range, not colon
            # Fourth mistake: take care of the interval range
            if haystack[possible :  possible+len(needle)] == needle:
                return possible
            else:
                i = possible+len(needle)
                
        #The method above seems jump len(needle) every time, that is not true, I still need to 
        while i < len(haystack):
            if haystack[i]== needle[0]:
            # mistake: I forget to use i+len(needle), I just use len(needle)
                if haystack[i:i+len(needle)] == needle:
                    return i
                 #mistake, firstly I didn't wright the else to increase i, then the while will not stop
                else:
                    i+=1
            else:
                i+=1
        return -1
        
   # more elegant one
   # https://leetcode.com/problems/implement-strstr/discuss/12814/My-answer-by-Python
   # same thought, but save a lot of time especially when needle has long length
