# https://leetcode.com/problems/word-ladder/description/

from collections import deque
from typing import List

# Zrobilem harda za pierwszym razem :D 
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    
    def valid(initialWord: str, expectedWord: str) -> bool:
        letterDifference = 0
        initialWordList = list(initialWord)
        expectedWordList = list(expectedWord)

        for i in range(len(initialWordList)):
            if initialWord[i] != expectedWordList[i]:
                letterDifference = letterDifference + 1

        return letterDifference < 2

    
    queue = deque([(beginWord, 1)])
    seen = set([beginWord])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps
        
        for wordFromList in wordList:
            if wordFromList not in seen and valid(word, wordFromList):
                queue.append((wordFromList, steps + 1))
                seen.add(wordFromList)
                wordList.remove(wordFromList)

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
