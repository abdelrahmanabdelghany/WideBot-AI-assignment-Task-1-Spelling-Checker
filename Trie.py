#list to map index to char
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class TrieNode:     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
        self.parent =None
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

        
 
class Trie:     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
        self.flag=False

    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return int(ord(ch)-ord('a'))
    
    def _IndexToChar(self,index):
         
        # private helper function
        # Converts index to char

        return alphabets[index]

    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not node.children[index]:
                node.children[index] = self.getNode()
                node.children[index].parent=node
            node = node.children[index]
 
        # mark last node as leaf
        node.isEndOfWord = True
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not node.children[index]:
                return False
            node = node.children[index]
 
        return node.isEndOfWord
    
    def _dfs(self,node,str,index):
        #helper function to do depth first search
        # visits alphabets in order 
        #index control from which letter we do the search so we can avoid finding same word
        #travese searching for next complete word in depth first search
        while index<25:
            if node.children[index]:
                str+=self._IndexToChar(index)
                if node.children[index].isEndOfWord:
                    self.next_words.append(str)
                    return True        
                else:
                    bool=self._dfs(node.children[index],str,0)
                    if bool:
                        return bool
                    str=str[0 : (len(str)-1)]                
            index+=1
        if str=="":
            return False      
        index=self._charToIndex(str[-1])+1      
        str=str[0 : (len(str)-1)]
        return self._dfs(node.parent,str,index)   
     
    
    def _get_next_word(self,key):
        # get where the word should be placed
        # get next by traversing with dfs
        node = self.root
        length = len(key)
        word=""
        for level in range(length):
            index = self._charToIndex(key[level])
            if  node.children[index]:
                node = node.children[index]
                word+=(self._IndexToChar(index))
            else: 
                #if prefix is not a word or part of a word in dictionary take a step back and start dfs with parent node
                #example
                ## if key =abc, and there is no word starts with abc 
                ## do depth first search for ab but search for letters afrer c (index+1)
                return self._dfs(node,word,index+1)    
        #if prefix is a word or part of a word in dictionary 
        # do do depth first search starting from letter a to z 
        return self._dfs(node,word,0)
        

    def _inv_dfs(self,node,str,index=25):
        #traverse with dfs but in reversed order of letters 
        #search for the previous word by taking a step back searshing with prefix[:-1]
        #starting from z to a dfs each option
        #index control from which letter we do the search so we can avoid finding same word
        #pool flag to indicate when a complete word is found so we continue traversing this path only 
        pool=False
        while index>-1:
            if node.children[index]: 
                pool=True
                str+=self._IndexToChar(index)
                self._inv_dfs(node.children[index],str,25)
            if pool:
                return
            else:
                index-=1
        if node.isEndOfWord:
            self.prev_words.append(str)
            return
        if str=="" :
            return 
        index=self._charToIndex(str[-1])-1
        str=str[0 : (len(str)-1)]     
        self._inv_dfs(node.parent,str,index) 

      

    def _get_prev_word(self,key):
        # get where the word should be placed
        # get prev by traversing with inv_dfs 
        
        node = self.root
        length = len(key)
        word=""
        #check if key is empty retun None
        if key=="":
            return None
        
        for level in range(length):
            index = self._charToIndex(key[level])
            if  node.children[index]:
                node = node.children[index]
                word+=(self._IndexToChar(index))
            else: 

                return self._inv_dfs(node,word,index-1)  
                  
        return self._inv_dfs(node.parent,word[:-1],index-1)
        


    def find_neighbors(self, key):
        # returns 4 words, the 2 words before and after this key in lexicographic order if they exist
        self.next_words=[]
        self.prev_words=[]
        #get the two words before key
        self._get_prev_word(key)
        if self.prev_words:
            self._get_prev_word(self.prev_words[0])
        #get the two words after key
        self._get_next_word(key)
        if self.next_words:
            self._get_next_word(self.next_words[0])

        return  self.prev_words+self.next_words


