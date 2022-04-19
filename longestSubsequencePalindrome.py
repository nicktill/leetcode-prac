class Solution(object):
#https://leetcode.com/problems/longest-palindromic-substring/ 
#LC Med, Commonly asked (Amazon)
    def longestPalindrome(self, s):
        outputString = ""
        for i in range(len(s)):
            #if we have an oddLength palindrome, the palindrome has one unique middle character 
            #I.E for 'racecar' => (rac'e'car) 'e' is unique middle character, and we can then go outwards using pointers to check Palindrome
            odd = self.palindrome(s, i, i)  #if palindrome odd, we must pass middle reference and increment left -=1, and right +=1
            
            #if we have an evenLength palindrome,  the palindrome has two unique middle character(s)
            #I.E for 'abba' => (a'bb'a) 'bb' are the two unique middle characters
            even = self.palindrome(s, i, i+1) 
            
            #return max of odd,even,outputString using the key comparison as length of substring
            #we know that the strings passed into odd and even are palindromes already, so simply compute max length 
            outputString = max(odd, even, outputString, key=len)

        return outputString
       
        
    #helper function to determine palindrome or not
    def palindrome(self,s,l,r):
        while(0<=l and r < len(s)) and (s[l]==s[r]):
                l-=1; r+=1
        return s[l+1:r] 