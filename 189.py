class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = [0] * n
        for i in range(n):
            new_index = (i + k) % n
            temp[new_index] = nums[i]
        for i in range(n):
            nums[i] = temp[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def reverse_sub(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverse_sub(0, n - 1)
        reverse_sub(0, k - 1)
        reverse_sub(k, n - 1)                    