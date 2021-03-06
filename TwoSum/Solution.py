
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDB = {}
        indexDB={}
        for i in range(len(nums)):
            if numDB.get(nums[i]) == None: #numDB.get worked but numDB[nums[i]] did not, wondering why.
                numDB[target-nums[i]]=nums[i]
                indexDB[target-nums[i]]=i
            else:
                return [indexDB[nums[i]],i]
            


sol = Solution()
nums = [-1,-2,2, 5, 10, 11]
target = 8
print(Solution.twoSum(sol, nums, target))
