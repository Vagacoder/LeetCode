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
    # insert word
    def insert(self, key: str) -> None:
        cur: TrieNode = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not cur.children[index]:
                cur.children[index] = self.createNode()
            cur = cur.children[index]
        cur.isEndOfWord = True

    def search(self, key: str) -> bool:
        cur: TrieNode = self.root
        length = len(key)

        for i in range(length):
            indexOfCurrentChar = ord(key[i]) - ord('a')
            if cur.children[indexOfCurrentChar]:
                cur = cur.children[indexOfCurrentChar]
            else:
                return False

        if cur.isEndOfWord:
            return True
        else:
            return False

    def delete(self, key: str) -> bool:
        cur: TrieNode = self.root
        length = len(key)
        for i in range(length):
            indexOfCurrentChar = ord(key[i]) - ord('a')
            if cur.children[indexOfCurrentChar]:
                cur = cur.children[indexOfCurrentChar]
            else:
                return False

        if cur.isEndOfWord:
            cur.isEndOfWord = False
            return True
        else:
            return False

    # helper function to print all words in trie, output is already sorted
    # usage: printSubTrie(rootNode of Trie, empty string"")
    def printSubTrie(self, startingNode: TrieNode, prevString: str) -> None:
        cur = startingNode

        if cur.isEndOfWord:
            print(prevString, '~end')

        for i in range(R):
            if cur.children[i]:
                currentChar = chr(i+ord('a'))
                newString = prevString + currentChar
                self.printSubTrie(cur.children[i], newString)


def main():

    # Set up different testing keys
    # keys = ['abcdefg']
    # keys = ['an', 'any']
    # keys = ['the', 'a', 'there', 'anaser', 'any', 'by', 'their']
    keys = ['the', 'a', 'banana', 'bye', 'there',
            'anwser', 'any', 'an', 'by', 'their']
    output = ['No Found', 'Found']
    output1 = ["Not Found", "Deleted"]
    # build a Trie for testing
    trie: Trie = Trie()
    for key in keys:
        trie.insert(key)

    # print Tries
    print()
    print('1. Print Whole Trie')
    trie.printSubTrie(trie.root, "")

    # Testing searching
    print('2. Testing Search Function')
    # print('Search {}, - expect: {} - my result: {}'.format("a",
    #                                                        "Found", output[trie.search("a")]))
    # print('Search {}, - expect: {} - my result: {}'.format("an",
    #                                                        "Found", output[trie.search("an")]))
    # print('Search {}, - expect: {} - my result: {}'.format("any",
    #                                                        "Found", output[trie.search("any")]))
    # print('Search {}, - expect: {} - my result: {}'.format("and",
    #                                                        "No Found", output[trie.search("and")]))
    # print('Search {}, - expect: {} - my result: {}'.format("at",
    #                                                        "No Found", output[trie.search("at")]))
    # print('Search {}, - expect: {} - my result: {}'.format("the",
    #                                                        "Found", output[trie.search("the")]))
    # print('Search {}, - expect: {} - my result: {}'.format("their",
    #                                                        "Found", output[trie.search("their")]))
    # print('Search {}, - expect: {} - my result: {}'.format("these",
    #                                                        "No Found", output[trie.search("these")]))
    # print('Search {}, - expect: {} - my result: {}'.format("to",
    #                                                        "No Found", output[trie.search("to")]))

    # Testing deletion
    print()
    print('3. Testing Delete Function')
    print('3.1 Before deletion')
    trie.printSubTrie(trie.root, "")
    print('Delete {}, - expect: {} - my result: {}'.format("the",
                                                           "Deleted", output1[trie.delete("the")]))
    print('3.2 After deletion "the"')
    trie.printSubTrie(trie.root, "")
    print('Delete {}, - expect: {} - my result: {}'.format("a",
                                                           "Deleted", output1[trie.delete("a")]))
    print('3.2 After deletion "a"')
    trie.printSubTrie(trie.root, "")


main()
