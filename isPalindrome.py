#Nicholas Tillmann, Short isPalindrome in Python Algorithm.
def isListPalindrome(l):
    
    palindromeList = []
    
    while l is not None:
        palindromeList.append(l.value)
        l = l.next

    return(palindromeList == palindromeList[::-1]) #::-1 reverses the list and checks if equal and returns true or false accordingly 

