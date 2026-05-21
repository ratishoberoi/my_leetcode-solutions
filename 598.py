class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        min_a=min(op[0] for op in ops)
        min_b=min(op[1] for op in ops)
        return min_a*min_b    
    

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        min_r = m
        min_c = n
        for r, c in ops:
            min_r = min(min_r, r)
            min_c = min(min_c, c)
        return min_r * min_c    