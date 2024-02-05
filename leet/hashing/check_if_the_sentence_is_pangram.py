# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
import string

input = "thequickbrownfoxjumpsoverthelazydog"
input2 = "leetcode"


def checkIfPangram(sentence: str) -> bool:
    letters = set(string.ascii_lowercase)
    for letter in letters:
        if letter not in sentence:
            return False

    return True


print(checkIfPangram(input))