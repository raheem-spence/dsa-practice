class Solution:

    def encode(self, strs: List[str]) -> str:
        # given: a list of strings
        # goal: return a single encoded string

        encoded_str = ""
        
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        l = 0

        while l < len(s):
            j = l

            while s[j] != "#":
                j += 1
            
            length = int(s[l:j])
            string = ""
            l = j + 1

            while length > 0:
                string += s[l]
                l += 1
                length -= 1
            decoded_strs.append(string)
        return decoded_strs

