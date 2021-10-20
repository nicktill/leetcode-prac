 def isPalindrome(self, s):
        string = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        revStr = string[::-1]
        return revStr == string
        
        