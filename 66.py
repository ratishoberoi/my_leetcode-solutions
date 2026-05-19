class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]
    

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Right se left ki taraf jaao
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits   # No carry, done
            
            # Agar 9 hai toh 0 kar do aur carry aage badhao
            digits[i] = 0
        
        # Agar yahan tak pahunche matlab pura number 999... tha
        return [1] + digits    