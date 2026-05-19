class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s=list(s)
        su=sum(shifts)
        for i in range(len(s)):
                ind=su%26
                ind=ord(s[i])+ind
                if(ind>122):
                    ind-=122
                    ind+=96
                s[i]=chr(ind)
                su-=shifts[i]
        return "".join(s)
