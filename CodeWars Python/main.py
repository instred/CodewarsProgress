import math


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

print(zeros(30))

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
