from typing import List

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

# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

key, value = 1, 1
obj = MyHashMap()
obj.put(key,value)
obj.put(key+1,value+1)
print(obj.get(key))
print(obj.get(3))
print(obj.show())
obj.put(2, 1)
print(obj.show())
obj.remove(2)
print(obj.show())
print(obj.get(2))

