class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        
        for index, character in enumerate(strs[0]):
            for word in strs:
                if index >= len(word) or character != word[index]:
                    return prefix
            prefix += character

            
        return prefix

            