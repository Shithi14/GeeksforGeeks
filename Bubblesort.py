#https://www.geeksforgeeks.org/problems/bubble-sort/1?page=2&category=Sorting&sortBy=accuracy

def bubblesort(arr, n):
    for i in range(0, n):
        swap=False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
                
        if not swap:
            print("The arry is before  swap")
            break
        
a = input()
arr = list(map(int, a.split()))
n = len(arr)
bubblesort(arr, n)
print("Sort Arry:",arr)