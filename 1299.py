#TLE AAYA ISMEI : 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            max=0
            for j in range(i+1,len(arr)):
                if arr[j]>max:
                    max=arr[j]
            arr[i]=max
        arr[-1]=-1
        return arr            
    
#ANOTHER METHOD:

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            original_val = arr[i]
            arr[i] = max_val
            if original_val > max_val:
                max_val = original_val
        return arr    