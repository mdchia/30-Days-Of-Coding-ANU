class Tries(): # Doesn't work. Left here for future reference
    def __init__(self):
        self.trie={"children":0}
    def add(self, word):
        curr_node=self.trie
        for letter in word:
            if letter in curr_node:
                curr_node["children"]+=1
                curr_node=curr_node[letter]
            else:
                curr_node[letter]={"children":1}
                curr_node=curr_node[letter]
    def find(self, word):
        curr_node=self.trie
        for letter in word:
            if letter in curr_node:
                curr_node = curr_node[letter]
            else:
                return 0
        return curr_node["children"]

class contacts(): # Uses n-gram style O(n) add, but O(1) lookup with dicts
    def __init__(self):
        self.contacts={}
    def add(self, word):
        s=""
        for l in word:
            s+=l
            if s in self.contacts:
                self.contacts[s]+=1
            else:
                self.contacts[s]=1
    def find(self, word):
        if word in self.contacts:
            return self.contacts[word]
        else:
            return 0

n = int(input().strip())
contacts=contacts()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op=="find":
        print(contacts.find(contact))
    if op=="add":
        contacts.add(contact)
