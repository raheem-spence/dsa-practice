class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for s in strs:
            encoded_str += str(len(s)) + "$" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1
            
            length = int(s[i:j])
            string = ""
            i = j + 1

            while length > 0:
                string += s[i]
                length -= 1
                i += 1

            decoded_strs.append(string)
        return decoded_strs    

