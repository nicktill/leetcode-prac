class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # Create a dictionary for the order of the alien alphabet
        alien_dict = {}
        #maps all characters
        #i,e order = abcdefghijklmnopqrstuvwxyz 
        #alien_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
        for i in range(len(order)):
            alien_dict[order[i]] = i
        
        # Compare each word to the next
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
            #if value of position'd letter in fWord less than respective letter in sWord break
                if alien_dict[word1[j]] < alien_dict[word2[j]]:
                    break
            #if value of position'd letter in fWord is greater than respective letter in sWord
            #return false, since this mean it is NOT sorted 
                elif alien_dict[word1[j]] > alien_dict[word2[j]]:
                    return False
        #otherwise return true 
        return True #set dictionary mapping keys
        
    

        