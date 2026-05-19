#BRUTE FORCE -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indices=[]
        for i in range(len(nums)):
            if nums[i]==target:
                indices.append(i)
        if indices :
            return [min(indices),max(indices)]
        else:
            return [-1,-1] 

#BRUTE FORCE - 2 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:      
                    first = i
                last = i             
        return [first, last]                   