# Q14. Extension 1, Trie
# Practice
R = 26


class TrieNode:

    def __init__(self):
        self.children = [None] * R
        self.value = ""
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def getNode(self) -> TrieNode:
        return TrieNode()

    def _charToIndex(self, char: str) -> int:
        return ord(char)-ord('a')

    # TODO: implement these 2 methods
    def insert(self, key: str) -> None:
        cur = self.root
        length = len(key)
        # for level in range(length):

    def search(self, key: str) -> str:
        return ""


def main():

    keys = ['the', 'a', 'there', 'anaser', 'any', 'by', 'their']
    output = ['No found', 'Found']

    trie = Trie()

    for key in keys:
        trie.insert(key)

    print('{} --- {}'.format("the", output[trie.search("the")]))


main()
