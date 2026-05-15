class Solution:
    def isValid(self, s: str) -> bool:
        
        st1 = []

        if len(s) == 1:
            return False

        for char1 in s:
            if char1 in set(["{", "[", "("]):
                st1.append(char1)

            print(st1)

            if char1 == "}":
                if st1 and st1[-1] == "{":
                    st1.pop()
                else:
                    return False

            if char1 == ")":
                if st1 and st1[-1] == "(":
                    st1.pop()
                else:
                    return False

            if char1 == "]":
                if st1 and st1[-1] == "[":
                    st1.pop()
                else:
                    return False

        return len(st1) == 0