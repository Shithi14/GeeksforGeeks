#https://www.geeksforgeeks.org/problems/palindrome-string0817/0

# User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase for case-insensitive comparison
        s = s.lower()
        # Check if the string is equal to its reverse
        return s == s[::-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Take input string
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Output true or false
        print("~")

# } Driver Code Ends
