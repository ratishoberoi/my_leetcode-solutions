#BRUTE FORCE : 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        for num in nums:
            if num != val:
                new_list.append(num)
        for i in range(len(new_list)):
            nums[i] = new_list[i]
        
        return len(new_list) 
    
#TWO POINTER APPROACH

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k     