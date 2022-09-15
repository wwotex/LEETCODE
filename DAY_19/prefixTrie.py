class Trie:
    class TreeNode:
        def __init__(self, val = 0):
            self.val = val
            self.finish = False
            self.children = {}



    def __init__(self):
        self.trie = self.TreeNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = self.TreeNode(letter)
            curr = curr.children[letter]
        curr.finish = True
        

    def search(self, word: str) -> bool:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.finish


    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
obj.insert('konga')
obj.insert('world')
obj.insert('wooing')
print(obj.search('word'))
print(obj.search('world'))
print(obj.search('wooing'))
print(obj.search('konga'))
print(obj.search('words'))
print(obj.search('wor'))
print(obj.search('abudabi'))
print(obj.startsWith('wor'))
print(obj.startsWith('wo'))
print(obj.startsWith('w'))
print(obj.startsWith('abd'))
print(obj.startsWith('words'))
print(obj.startsWith('word'))
# param_3 = obj.startsWith(prefix)