class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end

            ch = word[i]

            # Case 1: normal letter
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

            # Case 2: dot → try all possibilities
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False

        return dfs(self.root, 0)