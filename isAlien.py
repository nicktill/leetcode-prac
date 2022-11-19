class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # Create a dictionary for the order of the alien alphabet
        alien_dict = {}
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
        return True#set dictionary mapping keys
        
    

        