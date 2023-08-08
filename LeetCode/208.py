#
# LeetCode
#
# Problem - 208
# URL - https://leetcode.com/problems/implement-trie-prefix-tree/
#

class TrieNode:
  def __init__(self):
    self.children = dict()
    self.wordEnd = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node = self.root
    for letter in word:
      if not letter in node.children:
        node.children[letter] = TrieNode()

      node = node.children[letter]

    node.wordEnd = True

  def search(self, word: str) -> bool:
    node = self.root
    for letter in word:
      if not letter in node.children:
        return False

      node = node.children[letter]

    return node.wordEnd

  def startsWith(self, prefix: str) -> bool:
    node = self.root
    for letter in prefix:
      if letter in node.children:
        node = node.children[letter]
      else:
        return False

    return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)