class DecodeWays:
    def numDecodings(self, s: str) -> int:
        res = [0 for i in range(len(s))]
        res[0] = 1 if int(s[0]) >= 1 and int(s[0]) <= 26 else 0

        for i in range(1, len(s)):
            s1 = s[i]
            s2 = s[i-1:i+1]

            if int(s1) >= 1 and int(s1) <= 9:
                res[i] += res[i-1]
            if int(s2) >= 10 and int(s2) <= 26:
                if i >= 2:
                    res[i] += res[i-2]
                else:
                    res[i] += 1

        return res[-1]

obj = DecodeWays()
s = '11103'
print(obj.numDecodings(s))