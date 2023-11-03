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


sol = Solution()
a = [2,3,5]
n = 5
print(sol.buildArray(a, n))