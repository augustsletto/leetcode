
class Solution(object):
    def reverse(self, x):
        
    
        imax = (1 << 31) - 1
        imin = (-1 << 31)
        
        
        
        
        
        if "-" in str(x):
            strx = str(x).replace("-", "")
            x = "-" + (strx[::-1])
            if int(x) > imax or int(x) < imin:
                x = 0
            return int(x)
        
        elif x > 0:
            x = str(x)[::-1]
            if int(x) > imax or int(x) < imin:
                x = 0
            return int(x)
        else:
            return 0
        
        


solution = Solution()

print(solution.reverse(x=153469))
