class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for index, letter in enumerate(strs[0]):
            for word in strs:
                if index >= len(word) or letter != word[index]:
                    return prefix
            prefix += letter
        return prefix






