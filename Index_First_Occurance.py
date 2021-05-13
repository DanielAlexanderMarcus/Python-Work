class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        length=len(needle)
        subst=""
        i=0
        while i<=len(haystack)-1:
            subst=haystack[i:i+length]
            if subst==needle:
                return i
            else: i=i+1
        return -1
