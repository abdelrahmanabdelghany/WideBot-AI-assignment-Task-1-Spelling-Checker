import os
from Trie import Trie
import re


class Spelling_Checker:  
    # Spelling_Checker class

    def __init__(self,Dictionary_path):

        #check if path exists
        assert os.path.isfile(Dictionary_path)== True, "File doesn't exist"

        # Trie object
        self.Trie=Trie()

        #read dictionary.txt and Construct trie
        print("reading dictionary")

        with open(Dictionary_path,errors="ignore") as f:
            while True:
                word = f.readline()
                if not word:
                    break
                #filter for only alphabets 
                word=re.sub("[^A-Za-z]","",word)
                #Insert word
                self.Trie.insert(word)
                
    

    def _update_dictionary(self):
        #updates dictionary.txt file
        #function to update dictionary.txt file
        #will need to traverse trie and save output
        pass

    
    def _check_word(self,word):

        #check if word is a string
        assert isinstance(word,str), "word dtybe should be str"
        #check if word only contains alphabets
        assert word.isalpha()== True, "word should contain only alphabets"
        #return filtered word
        word=re.sub("[^A-Za-z]","",word)
        word=word.lower()
        return word  

    def Insert(self,word):

        #check if word is valid
        word=self._check_word(word)     

        #check if word already in dictionary
        if self.Trie.search(word):
            print("word already exists")
        else :
            #insert word 
            self.Trie.insert(word)
            print(word," is inserted successfully")
            #update and save dictionary
            ##_update_dictionary()
    
    def Find_4_Nearest_words(self,word):
        #check if word is valid
        word=self._check_word(word)
        #Search for word
        if self.Trie.search(word):
            print("word already exists")
            return None
        else :
            #Get 4 Nearest words
            Nearest_words=self.Trie.find_neighbors(word)
            print("The 4 Nearest words to " , word, " are",Nearest_words)
            return Nearest_words

        





            