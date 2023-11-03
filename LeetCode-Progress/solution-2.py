from typing import List

# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:
#     "Push": pushes an integer to the top of the stack.
#     "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].
# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target

# 89/44%
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        idx_tab = 0
        for i in range(1, n+1):
            if i == target[idx_tab]:
                res.append("Push")
                if idx_tab != len(target)-1:
                    idx_tab += 1
                else:
                    return res
            else:
                res.append("Push")
                res.append("Pop")
        return res


# 86/95%
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        
        for num in target:
            while i < num - 1:
                ans.append("Push")
                ans.append("Pop")
                i += 1

            ans.append("Push")
            i += 1

        return ans
    
# You are given an array nums of positive integers and an integer k.
# In one operation, you can remove the last element of the array and add it to your collection.
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.

# 72/39%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        stack = []
        while len(stack) != k:
            p = nums.pop()
            if p <= k and p not in stack:
                stack.append(p)
            ans += 1
        return ans


# 50/72%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        occ = [0] * k
        while 0 in occ:
            p = nums.pop()
            if p <= k:
                occ[p-1] = 1
            ans += 1
        return ans
    

sol = Solution()
nums = [3,1,5,4,2]
k = 2
print(sol.minOperations(nums, k))