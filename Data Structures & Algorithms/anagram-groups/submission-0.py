class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            alphabet = [0] * 26
            for c in string:
                index = ord(c) - ord('a')
                alphabet[index] += 1
            anagrams.setdefault(tuple(alphabet), []).append(string)
        return list(anagrams.values())
