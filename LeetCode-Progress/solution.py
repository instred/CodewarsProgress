from typing import List
from math import floor
from collections import Counter
import pandas as pd
import numpy as np


#Given an integer n, return true if it is a power of four. Otherwise, return false.
#An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n % 4 == 0:
            n = n / 4
        if n == 1:
            return True
        return False
    
#same but with bit checking for n is power of 2 + n%3 == 1 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n >0 and n & (n-1) == 0 and n%3 == 1

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        output = [word[::-1] for word in words]
        return " ".join(output)



# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.
# Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.
# Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
# Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.


class Solution:
    def counterr(self, colors, player) -> int:
        i, alles, suma = 0, 0, 0
        while i < len(colors):
            if colors[i] == player:
                suma += 1
            else:
                suma = 0 
            i += 1
            if suma >= 3:
                alles += suma-2
        return alles


    def winnerOfGame(self, colors: str) -> bool:
        alice = self.counterr(colors, player="A")
        bob = self.counterr(colors, player="B")
        return True if alice > bob else False
        
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_score, b_score = 0, 0
        for i in range(1, len(colors)-1):
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                a_score +=  1
            if colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                b_score +=  1
        return True if a_score > b_score else False


# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myset = [0] * 100
        summ, c = 0, 1
        for num in nums:
            summ += myset[num]
            myset[num] += 1
        return summ
    

# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


class MyHashMap:

    def __init__(self):
        self.hashmap = [None] * 1001

    def put(self, key: int, value: int) -> None:
        if self.hashmap[key] is not None:
            self.hashmap[key] = value
        else:
            self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key] if self.hashmap[key] is not None else -1


    def remove(self, key: int) -> None:
        if self.hashmap[key] is not None:
            self.hashmap[key] = None

    def show(self) -> List[int]:
        return self.hashmap


# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

global values

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:

    def helper(self, res: List[int], root : TreeNode, height: int) -> None:
        if not root:
            return
        
        if height == len(res):
            res.append(root.val)
        else:
            res[height] = max(root.val, res[height])

        self.helper(res, root.left, height+1)
        self.helper(res, root.right, height+1)


    def largestValues(self, root: [TreeNode]) -> List[int]:
        res = []
        self.helper(res, root, 0)
        return res


                #       1
                #      / \
                #     3   2
                #    / \   \ 
                #   5   3   9


# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = floor(len(nums)/3)
        numbers = {}
        for num in nums:
            if num in numbers and numbers[num] <= limit:
                numbers[num] += 1
            elif num not in numbers:
                numbers[num] = 1
        return [x for x in numbers if numbers[x] > limit]
    

class Solution:
    def majorityElements(self, nums: List[int]) -> List[int]:
        return [x for x, count in Counter(nums).items() if count > len(nums) // 3]


# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return res * n


# You should build the array arr which has the following properties:
# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.


class Solution:
    def binSearchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) -1
        while l <= r:
            half = l + (r-l) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                l = half + 1
            else:
                r = half - 1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = self.binSearchRange(nums, target)
        print(idx)
        l, r = None, None
        if idx == -1:
            return [-1, -1]
        for i in range(idx + 1, len(nums)):
            if nums[i] > target:
                r = i-1
                break
        for i in range(idx -1, -1, -1):
            if nums[i] < target:
                l = i+1
                break
        if l is None:
            l = 0
        if r is None:
            r = len(nums)-1
        return [l, r]
    

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums: List[int], target: int):
            l = 0
            r = len(nums) -1
            while l <= r:
                half = l + (r-l) // 2
                if nums[half] == target:
                    if half == 0 or nums[half - 1] != target:
                        return half
                    else:
                        r = half - 1
                elif nums[half] < target:
                    l = half + 1
                else:
                    r = half - 1
            return -1
    
        def find_last(nums: List[int], target: int):
            l = 0
            r = len(nums) -1
            while l <= r:
                half = l + (r-l) // 2
                if nums[half] == target:
                    if half == len(nums) - 1 or nums[half + 1] != target:
                        return half
                    else:
                        l = half + 1
                elif nums[half] < target:
                    l = half + 1
                else:
                    r = half - 1
            return -1
        return [find_first(nums, target), find_last(nums, target)]
    
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [None] * len(cost)
        dp[len(cost) - 1] = cost[len(cost)-1]
        dp[len(cost) - 2] = cost[len(cost)-2]
        for i in range(len(cost) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        
        return min(dp[0], dp[1])

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row_b, row = [1], [1]
        for i in range(0,rowIndex):
            for i, num in enumerate(row_b):
                if i+1 != len(row_b):
                    row.append(num+row_b[i+1])
                else:
                    row.append(num)
            row_b = row
            row = [1]
        return row_b
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            row[i] = row[i-1] * (rowIndex - i + 1) // i
        return row


# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.


# 0
# 0 1
# 0 1 1 0
# 0 1 1 0 1 0 0 1
# 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
# 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1 
# 


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        is_same = True

        #calc numbers in row
        n = 2**(n-1)

        while n != 1:
            #cut in half to get number count in half
             n //= 2

            #if k > this number -> k is in the second half so we move it to the first with reversing flag
             if k > n:
                is_same = not is_same
                k -= n

        return 0 if is_same else 1


# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.


class Solution:

    def printPreorder(self, root, left, right, visited):
        
        print(root)
        if root != -1 and root in visited:
            return False

        if root != -1:
            visited.append(root)
            self.printPreorder(left[root], left, right, visited)
            self.printPreorder(right[root], left, right, visited)
        elif root == -1:
            visited.append(-1)
        return visited

            
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = None
        visited = []
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                root = i
                break
        if root is None:
            return False
        visited = self.printPreorder(root,leftChild, rightChild, visited)
        print(visited)
        if len(visited)-1!= (len(leftChild) + len(rightChild)):
            return False
        return True

# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        pass



# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while True:
            pos = s.find('#')
            pos2 = t.find('#')
            if pos == -1 and pos2 == -1:
                break
            if pos != -1:
                if pos == 0:
                    s = s[1:]
                else:
                    s = s[:pos-1] + s[pos+1:] 
            if pos2 != -1:
                if pos2 == 0:
                    t = t[1:]
                else:
                    t = t[:pos2-1] + t[pos2+1:] 
        return s == t

# stack solution

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for let in s:
            if let == '#' and stack:
                stack.pop()
            elif let != '#':
                stack.append(let)
        s = ''.join(stack)
        stack = []
        for let in t:
            if let == '#' and stack:
                stack.pop()
            elif let != '#':
                stack.append(let)
        t = ''.join(stack)
        return s, t
    

# The Leetcode file system keeps a log each time some user performs a change folder operation.
# The operations are described below:
#     "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
#     "./" : Remain in the same folder.
#     "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
# The file system starts in the main folder, then the operations in logs are performed.
# Return the minimum number of operations needed to go back to the main folder after the change folder operations.


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for opp in logs:
            if stack and opp == "../":
                stack -= 1
            elif opp == "./":
                pass
            elif opp != "../":
                stack += 1
        return stack


# Write a solution to display the first 3 rows of this DataFrame.


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  | 
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+


# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+

# A company intends to give its employees a pay rise.
# Write a solution to modify the salary column by multiplying each salary by 2.

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x: x*2)
    # employees['salary'] *= 2
    # employees['salary'] = employees['salary'].transform(lambda x: x*2)
    return employees




# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation 
# and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the array after sorting it.


class Solution:
    def checkones(self, n: int) -> int:
        count = 0
        while n > 0:
            count = count + 1
            n = n & (n-1)
        return count


    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (self.checkones(x), x))
        return arr
            
# "little" shorter xdd

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))




soll = Solution()
arr = [0,1,2,3,4,5,6,7,8]
arr2 = [1024,512,256,128,64,32,16,8,4,2,1]
arr3 = [1000, 1000]
print(soll.sortByBits(arr))