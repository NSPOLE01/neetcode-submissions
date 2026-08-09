class PrefixTree:

    def __init__(self):
        self.words = set()
        self.prefixes = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        i = 0
        for j in range(len(word)):
            self.prefixes.add(word[i:j])

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes:
            return True
        return False
        
        