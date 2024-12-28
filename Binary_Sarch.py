# https://www.geeksforgeeks.org/problems/binary-search-1587115620/0
#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        
        # Code Here
        n=len(arr)
        left=0
        right=n-1
        search=-1
       
        while left<=right:
            mid=left+(right-left)//2
            
            
            if arr[mid]==k:
                search=mid
                right=mid-1
                
                
            elif arr[mid]<k:
                    left=mid+1
                    
            else:
                right=mid-1
                
                
        return search
                
                


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends