#https://www.geeksforgeeks.org/problems/selection-sort/1?page=2&category=Sorting&sortBy=accuracy

def selection_sort(arr, n):
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]


a = input()


arr = list(map(int, a.split())) 
n = len(arr)
selection_sort(arr, n)
print("Sorted: ",arr)