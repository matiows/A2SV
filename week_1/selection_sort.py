#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minInx = i
        for index in range (i, len(arr)-1):
            if arr[index+1]<arr[minInx]:
                minInx = index+1
        return minInx
    
    def selectionSort(self, arr,n):
        for index in range(0, len(arr)-1):
            minInx = self.select(arr, index)
            arr[index], arr[minInx] = arr[minInx], arr[index]

        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends