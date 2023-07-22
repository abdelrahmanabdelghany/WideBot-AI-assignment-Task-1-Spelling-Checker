# WideBot-AI-assignment-Task-1-Spelling-Checker
# implement a spell checker class that takes this dictionary as input, this class has three main operations:
  • Store this dictionary in a suitable data structure.
  • Take an input word and return the nearest 4 words if this word is not in the dictionary
  • Take an input word and add this word to the dictionary

## time and space complexity
### Storing the dictionary time complexity O(N * m) where N num of words and m word length since m is reletivly small we can say O(N), space complexity  O(26 * Numberofwords * avg_wordlength) , 26=num of alphabets.
   
###  Nearest 4 words search time complexity O(N) for search and O(N) for traversal I'm not sure feels like O(26 * N), space complexity O(1).

### Insertion time complexity O(N) we need to visit N nodes where N =length of word, Space complexity O(N) where N num of nodes to be created maximum length of word.
