# Q14. Extension 1, Trie
# Practice
R = 26


class TrieNode:

    def __init__(self):
        self.children = [None] * R
        self.value = ""
        self.isEndOfWord = False

    def isEndNode(self) -> bool:
        for child in self.children:
            if child != None:
                return False
        return True


class Trie:

    def __init__(self):
        self.root = self.createNode()

    def createNode(self) -> TrieNode:
        return TrieNode()

    def _charToIndex(self, char: str) -> int:
        return ord(char)-ord('a')

    # TODO: implement these  methods

    def insert(self, key: str) -> None:
        cur: TrieNode = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not cur.children[index]:
                cur.children[index] = self.createNode()
            cur = cur.children[index]
        cur.isEndOfWord = True

    def search(self, key: str) -> str:
        return ""

    def delete(self, key: str) -> bool:
        return False

    def printTrie(self) -> str:
        return ""


def main():

    keys = ['the', 'a', 'there', 'anaser', 'any', 'by', 'their']
    output = ['No found', 'Found']

    trie = Trie()

    for key in keys:
        trie.insert(key)

    # print('{} --- {}'.format("the", output[trie.search("the")]))


main()
