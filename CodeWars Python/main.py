import math
import string 
from collections import Counter
import re
from dataclasses import dataclass
from typing import List, Tuple




# Build Tower by the following given arguments:
#     number of floors (integer and always greater than 0)
#     block size (width, height) (integer pair and always greater than (0, 0))


def tower_builder(n_floors : int, block_size : Tuple[int, int]) -> List[str]:
    tower = []
    stars = block_size[0]
    for i in range(n_floors-1, -1, -1):
        for j in range(block_size[1]):
            tower.append(f'{(i*block_size[0]) * " "}{stars * "*"}{(i*block_size[0]) * " "}')
        stars += block_size[0]*2
    return tower

print(*tower_builder(3, (2,3)), sep="\n")

# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string. The input string can be assumed to 
# contain only alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text : str) -> int:
    d_count = {}
    for chr in text.lower():
        if chr in d_count:  
            if d_count[chr] == 0:
                d_count[chr] += 1
        else:
            d_count[chr] = 0
    return sum(d_count.values())


# find list outlier

def find_outlier(integers : List[int]) -> int:
    # i = 0
    # while i < len(integers):
    #     if (integers[i] + integers[i+1]) % 2 != 0:
    #         return integers[i] if (integers[0] + integers[2]) % 2 != 0 else integers[i+1]
    #     i += 1

    odds = [x for x in integers if x % 2 != 0]
    even = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) < len(even) else even[0]



# create phone number

def create_phone_number(n : List[int]) -> str:
    # return f'({"".join(map(str, n[:3]))}) {"".join(map(str, n[3:6]))}-{"".join(map(str, n[6:10]))}'
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



# array diff

def array_diff(a : List[int], b : List[int]) -> List[int]:
    for num in b:
        a = [i for i in a if i != num]
        # a = list(filter((num).__ne__, a))
    return a
    # return [num for num in a if num not in b]



# return likes count

def likes(names : List[str]) -> str:

    match(names):
        case []:
            return "no one likes this"
        case [a]:
            return f"{a} likes this"
        case [a, b]:
            return f"{a} and {b} like this"
        case [a, b, c]:
            return f"{a}, {b} and {c} like this"
        case [a, b, *rest]:
            return f"{a}, {b} and {len(rest)} like this"


# return digital root of a number

def digital_root(n : int) -> int:
    if len(str(n)) == 1:
        return n
    return digital_root(sum(int(l) for l in str(n)))



# reverse > 5 letter words

def spin_words(sentence : str) -> str:
    words = sentence.split(" ")
    words_new = []
    for word in words:
        if len(word) >= 5:
            words_new.append(word[::-1])
        else:
            words_new.append(word)
    return " ".join(words_new)

# vovels count

def get_count(sentence : str) -> int:
    counter = 0
    vovels = {"a", "e", "i", "o", "u"}
    for letter in sentence:
        if letter in vovels:
            counter += 1
    return counter

# even or odd

def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    return "Odd"



#height of binary tree

    #          5
    #       /     \d
    #      3       10
    #     / \     /       
    #   20  21   1     

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

def s4(T):
    if T is None:
        return 0
    
    if T.l is not None:
        ld = s4(T.l)

    if T.r is not None:
        rd = s4(T.r)
    maxx = ld if ld > rd else rd
    return maxx+1


# that, given a string S, returns the index (counting from 0) of a character such that the part of the string
# to the left of that character is a reversal of the part of the string to its right. 
# The function should return −1 if no such index exists.


def s3(S):
    if len(S) % 2 == 0:
        return -1
    if len(S) == 1:
        return 0
    mid = len(S) // 2
    r = S[mid+1:len(S)]
    if S[0:mid] == r[::-1]:
        return mid
    return -1


# Write a function:
# that, given a non-empty array A of N integers, returns the first unique number in A. 
# The function should return −1 if there are no unique numbers in A.


def s2(A):
    dictt = {}
    for x in A:
        if x not in dictt:
            dictt[x] = 1
        else:
            dictt[x] += 1
    for x in dictt:
        if dictt[x] == 1:
            return x
    return -1

#smallest number that is not in list

def s(A):
    dict = {}
    for x in A:
        if x > 0:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1

    for i in range(1,1000000):
        if i not in dict:
            return i
    

# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    ans =  '#'+''.join(s.title().split())
    if len(ans) > 140 or ans == '#':
        return False
    return ans

# Write a function that, given a string of text (possibly with punctuation and line-breaks), 
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]


# Write two functions that convert a roman numeral to and from an integer value. 
# Multiple roman numeral values will be tested for each function.

def val(s):
    match s:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000

class RomanNumerals:
    @staticmethod
    def to_roman(val):
        ans = ""
        letter_val = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 
                      40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV'}
        while(val >= 4):
            for l in letter_val:
                if val // l >= 1 :
                    ans += (val // l) * letter_val[l]
                    val %= l
        return ans+val*'I'



    @staticmethod
    def from_roman(roman_num):
        ans = 0
        i = 0 
        while i < len(roman_num):
            if i == len(roman_num) - 1:
                return ans + val(roman_num[i])
            if val(roman_num[i]) < val(roman_num[i+1]):
                ans += val(roman_num[i+1]) - val(roman_num[i])
                i += 2
                continue
            ans += val(roman_num[i])
            i += 1
        return ans


# Write a method (or function, depending on the language) that converts a string to camelCase, 
# that is, all words must have their first letter capitalized and spaces must be removed.

def camel_case(s):
    ans= s.title().replace(" ", "")
    return ans


# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

#can do just this recursively

def zeros_easier(n):
  x = n/5
  return x+zeros(x) if x else 0

def zeros(n):
    if n == 0:
        return 0
    sum = 0
    kmax = math.log(n,5)
    for i in range(1, int(kmax)+1):
        sum += math.floor(n/(5**i))
    return sum

# Write a simple parser that will parse and run Deadfish.
# Deadfish has 4 commands, each 1 character long:
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

def parse(data):
    ans = []
    val = 0
    for l in data:
        match l:
            case 'i':
                val+=1
            case 'd':
                val -=1
            case 's':
                val = val**2
            case 'o':
                ans.append(val)
    return ans

# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
# You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

def wave(people):
    ans = []
    for i in range(len(people)):
        if (people[i] == " "):
            continue
        ans.append(people[:i]+people[i:].capitalize())
    return ans

# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. 
# Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

def diamond(n):
    if n < 0 or n%2 == 0:
        return None
    if n == 1:
        return "*\n"
    mid = (n+1)/2
    ans = []
    strg = ""
    i = 1
    while mid != 0:
        ans.append((int(mid)-1)*" " + i*"*" +"\n")
        mid -= 1
        i += 2
    for i in range(len(ans)-1):
        strg += ans[i]
    for i in range(len(ans)-1, -1, -1):
        strg += ans[i]
    return strg


# Given a positive number n > 1 find the prime factor decomposition of n. 
# The result will be a string with the following form :
#  "(p1**n1)(p2**n2)...(pk**nk)"

# best practise
def prime_factors(n):
    ans = ""
    divisor = 2
    while n != 1:
        count = 0
        while n%divisor == 0:
            n /= divisor
            count += 1
        if count == 0:
            pass
        elif count == 1:
            ans += f"({divisor})"
        else:
            ans += f"({divisor}**{count})"
        divisor += 1
    return ans


# Define a function that takes an integer argument 
# and returns a logical value true or false depending on if the integer is a prime.

def is_prime(num):
    if num<0 or num == 0 or num == 1:
        return False
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

def is_valid_IP(strng):
    piece = strng.split('.')
    if(len(piece) != 4):
        return False
    for x in piece:
        if len(x)>1 and x[0] == '0':
            return False
        if not x.isnumeric():
            return False
        if int(x) < 0 or int(x) > 255:
            return False
    return True


# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.

def order(sentence):
    tmp = {}
    ans = ""
    chara = 0
    for i in range(len(sentence)):
        if sentence[i].isnumeric():
            place = sentence[i]
        if sentence[i] == " ":
            tmp[place] = sentence[chara:i]
            chara = i + 1
        if i == len(sentence) - 1:
            tmp[place] = sentence[chara:i + 1]
    tmp = dict(sorted(tmp.items()))
    for x in tmp:
        ans += tmp.get(x) + " "
    return ans.strip()


# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information
# consists of an integer for the person's age and an integer for the person's handicap. Output will consist of a list
# of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the
# senior or open category.

def open_or_senior(data):
    output = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")

    return output


# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.


def alphabet_position(text):
    answ = ""
    text = text.lower()
    for i in range(len(text)):
        if text[i].isalpha():
            answ += " "
            answ += str(string.ascii_lowercase.index(text[i]) + 1)
    return answ[1:]


# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
# that character appears only once in the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    word = word.lower()
    dictt = {}
    ans = ""
    for x in word:
        if x in dictt:
            dictt[x] += 1
        else:
            dictt[x] = 1
    for x in word:
        if dictt[x] > 1:
            ans += ")"
        else:
            ans += "("
    return ans
