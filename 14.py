# BRUTE FORCE

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        first = strs[0]
        n = len(first)
        
        for i in range(n + 1):           
            prefix = first[:i]
            for s in strs[1:]:
                if not s.startswith(prefix):
                    return first[:i-1]   
        return first
    
# HORIZONTAL SCANNING 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]      
                if not prefix:
                    return ""
        return prefix
    
# VERTICAL SCANNING

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
         return ""
        
        for i in range(len(strs[0])):          
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]
    
# Sorting + First & Last String Compare 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()                    
        first, last = strs[0], strs[-1]
        min_len = min(len(first), len(last))
        
        for i in range(min_len):
            if first[i] != last[i]:
                return first[:i]
        return first[:min_len]

