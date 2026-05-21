class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []
        for num in nums:
            if num != 0:
                temp.append(num)
        while len(temp) < len(nums):
            temp.append(0)
        for i in range(len(nums)):
            nums[i] = temp[i]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
            
                        