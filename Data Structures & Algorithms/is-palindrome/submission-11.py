class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = ""

        for char in s:
            if char != " " and char.isalnum():
                temp += (char.lower())

        print(temp)
    
        return (temp == temp[::-1])