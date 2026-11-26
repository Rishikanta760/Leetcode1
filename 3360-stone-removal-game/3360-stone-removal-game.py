class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=10
        while n>=i and i>0:
            n-=i
            i-=1
        return i%2==1