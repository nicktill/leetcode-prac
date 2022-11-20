class Solution(object):
    def isAlienSorted(self, words, order):
        #order = abcdefgh 
        #words = [hello, hey, hi]
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i #update order of list with respective mappings to 0-N Characters
        

        #hello, #herfjxojc
        for i in range(len(words)-1):
            word1 = words[i] #first letter o
            word2 = words[i+1] #first letter of second word
            #iterate over the first word1
            for j in range(len(word1)):
                if j >= len(word2): #check if the index of J (length of word1), is larger than word2, if so,
                    #that means that first word is longer
                    return False
                    #if first index of first word, greater than second value, break
                if alien_dict[word1[j]] > alien_dict[word2[j]]: 
                    break 
                    #if first
                elif alien_dict[word1[j]] < alien_dict[word2[j]]: 
                    return False 

            return True #otherwise, return true 
                
