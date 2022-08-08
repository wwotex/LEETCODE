class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_fin = []
        t_fin = []
        self.populate(s, s_fin)
        self.populate(t, t_fin)
        return s_fin == t_fin
            
    def populate(self, s, s_fin):
        for el in s:
            if el == '#':
                if s_fin:
                    s_fin.pop()
            else:
                s_fin.append(el)
            