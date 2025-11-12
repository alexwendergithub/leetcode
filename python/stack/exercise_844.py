class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        tt = []
        for charachter in s:
            if charachter == "#":
                if len(st):
                    st.pop()
            else:
                st.append(charachter)
        for charachter in t:
            if charachter == "#":
                if len(tt):
                    tt.pop()
            else:
                tt.append(charachter)
        return ''.join(st) == ''.join(tt)