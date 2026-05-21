class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for n in nums:
            if len(str(n)) % 2 ==0:
                count+=1
        return count
                
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for n in nums:
            digits=0
            while n > 0 :
                n=n//10
                digits+=1
            if digits % 2 ==0 :
                count+=1
        return count                             