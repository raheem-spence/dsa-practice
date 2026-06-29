class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += str(n) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return decoded

        # Time --> O(n) one pass through strings
        # Space --> O(m + n), m is the sum of lengths of all strings, n is
        # the number of strings
