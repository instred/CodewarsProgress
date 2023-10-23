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


colors = "AAABABB"
sol = Solution()
print(sol.winnerOfGame(colors))

