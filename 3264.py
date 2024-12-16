# Given integer array "nums" and integer "k" and integer "multiplier"
# perform "k" operations on nums, in each:
# fins minimum value in nums, if multiple occurences of minval, select the first one
# Replace min val "x" with "x * multiplier




class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        
        

        for i in range(k):
            index = nums.index(min(nums))

            nums[index] = min(nums) * multiplier
        return nums
    

solution = Solution()

    
result = solution.getFinalState(
    nums = [2, 1, 3, 5, 6],
    k=5,
    multiplier=2)

print(result)