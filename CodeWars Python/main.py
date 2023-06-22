import string


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
