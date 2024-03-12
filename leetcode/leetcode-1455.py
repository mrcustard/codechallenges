#!/usr/bin/env python3

# read a file and determine if a word in a line starts with a prefix

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        indexOfWords = []
        for index, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                indexOfWords.append(index + 1)
        if len(indexOfWords) == 0:
            return -1
        else:
            return min(indexOfWords)

    def isPrefixOfWord2(self, sentence: str, searchWord: str) -> int:
        sw = sentence.split()
        for i in range(len(sw)):
            if sw[i][0] == searchWord[0]:
                if sw[i][:len(searchWord)] == searchWord:
                    return i + 1
        return -1


s = Solution()
print(s.isPrefixOfWord2("i love eating burger", "burg"))
print(s.isPrefixOfWord2("this problem is an easy problem", "pro"))
print(s.isPrefixOfWord2("i am tired", "you"))
