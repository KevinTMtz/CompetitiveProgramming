#
# LeetCode
#
# Problem - 211
# URL - https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#

class WordDictionary:
  def __init__(self):
    self.trie = dict()
    self.longest = 0

  def addWord(self, word: str) -> None:
    self.longest = max(self.longest, len(word))

    tempTrie = self.trie
    for i in range(len(word)):
      if not word[i] in tempTrie:
        tempTrie[word[i]] = dict()
        tempTrie[word[i]]['end'] = False

      tempTrie = tempTrie[word[i]]
    
    tempTrie['end'] = True

  def search(self, word: str) -> bool:
    if self.longest < len(word):
      return False

    return self.searchHelper(word, self.trie)

  def searchHelper(self, word: str, trie: dict) -> bool:
    lastLetter = len(word) == 1
    if word[0] == '.':
      for key in trie.keys():
        if key != 'end' and (
            (lastLetter and trie[key]['end']) or 
            (not lastLetter and self.searchHelper(word[1:], trie[key]))
          ):
          return True
    elif word[0] in trie:
      if lastLetter:
        return trie[word[0]]['end']
      else:
        return self.searchHelper(word[1:], trie[word[0]])

    return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
