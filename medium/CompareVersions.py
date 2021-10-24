'''
https://leetcode.com/problems/compare-version-numbers/
Given two version numbers, version1 and version2, compare them.
'''
class CompareVersions:
    def compareVersion(self, version1: str, version2: str) -> int:
        res = 0

        v1 = [int(st) for st in version1.split(".")]
        v2 = [int(st) for st in version2.split(".")]
        for i in range(max(len(v1), len(v2))):
            if i >= len(v1):
                v1.append(0)
            if i >= len(v2):
                v2.append(0)

            if v1[i] > v2[i]:
                res = 1
                return res
            elif v2[i] > v1[i]:
                res = -1
                return res
            else:
                res = 0

        return res

obj = CompareVersions()
version1 = "1.0.1"
version2 = "1"
print(obj.compareVersion(version1, version2))