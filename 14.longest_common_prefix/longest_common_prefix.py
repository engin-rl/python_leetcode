class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            prefix += char

        return prefix


Solution().longestCommonPrefix(["flower", "flow", "flight"])


# Solution().longestCommonPrefix(["dog", "racecar", "car"])
