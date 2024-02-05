def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazineDictionary = {}
    for letter in magazine:
        if magazineDictionary.get(letter) is not None:
            magazineDictionary[letter] += 1
        else:
            magazineDictionary[letter] = 1

    for note in ransomNote:
        if magazineDictionary.get(note) is not None:
            if magazineDictionary[note] == 1:
                magazineDictionary.pop(note)
            else:
                magazineDictionary[note] -= 1
        else:
            return False

    return True


print(canConstruct("aa", "ab"))