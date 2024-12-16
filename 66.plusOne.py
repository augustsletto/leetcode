# digits = [9]


# s = ""

# for i in range(len(digits)):
#     s += str(digits[i])

# int = int(s) + 1

# print(int)


class Solution(object):
    def plusOne(self, digits):
        finished = []
        s = ""
        
        for i in range(len(digits)):
            s += str(digits[i])
            
        to_list = str(int(s) + 1)
        
        
        for ch in to_list:
            finished.append(int(ch))
            
        return finished
        
solution = Solution()

print(solution.plusOne([1, 2, 3, 4]))