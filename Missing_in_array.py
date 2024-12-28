#https://www.geeksforgeeks.org/problems/missing-number-in-array1416/0
#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code heres
        n=len(arr)+1
        sum=(n*(n+1))//2
        sum1=0
        for i in range(0,len(arr)):
            sum1=sum1+arr[i]
        s=sum-sum1
        return s
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends