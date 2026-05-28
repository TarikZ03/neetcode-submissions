class Solution:

    def encode(self, strs: List[str]) -> str:

        out = ""
        delim="#"

        for s in strs:
            out += f"{len(s)}{delim}{s}" 
        return out
            
    def decode(self, s: str) -> List[str]:
        
        out = []

        while len(s) != 0:            
            d_idx = s.find("#")
            num_char = int(s[:d_idx])
            word = s[d_idx + 1 : num_char + d_idx + 1]
            out.append(word)
            s = s[num_char + d_idx + 1:]

        return out


