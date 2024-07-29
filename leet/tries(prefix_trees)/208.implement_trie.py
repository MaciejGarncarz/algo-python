# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.data = []
        self.children = {}
        

    def insert(self, word: str) -> None:
        curr = self
        curr.data.append(word)
        for character in word:
            if character not in curr.children:
                curr.children[character] = Trie()
            curr = curr.children[character]
            curr.data.append(word)
        

    def search(self, word: str) -> bool:
        curr = self
        if word in curr.data:
            return True
        for character in word:
            if character not in curr.children:
                return False
            curr = curr.children[character]
            
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for character in prefix:
            if character not in curr.children:
                return False
            curr = curr.children[character]
        
        return True

        

trie = Trie()
trie.insert("app")
trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rentral")
# trie.search("apple")
# trie.search("app")
# trie.startsWith("app")
# trie.insert("app")
# trie.search("app")