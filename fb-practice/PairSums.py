
def numberOfWays(arr, k):
    arr.sort()
    freq = {}
    res = 0

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    i, j = 0, len(arr)-1
    while i < j:
        if arr[i] + arr[j] == k:
            a = freq[arr[i]]
            b = freq[arr[j]]

            if arr[i] == arr[j]:
                if a == 2:
                    res += 1
                else:
                    res += (a*(a-1)//2)
            else:
                res += (a * b)
            while arr[i+1] == arr[i]:
                i += 1
            while arr[j-1] == arr[j]:
                j -= 1

            i += 1
            continue
        elif arr[i] + arr[j] < k:
            i += 1
        else:
            j -= 1
    return res

def numberOfWays2(arr, k):
    res = 0
    freq = {}
    seen_half = False
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in arr:
        if k%2 == 0 and i == k//2:
            if not seen_half:
                res += (freq[k//2] * (freq[k//2]-1)//2)
                seen_half = True
            else:
                continue
        else:
            if k-i in freq:
                a = freq[i]
                b = freq[k-i]
                del freq[i]
                del freq[k-i]
                res += (a*b)

    return res


arr = [1, 5, 3, 3, 3]
k = 6
print(numberOfWays2(arr,k))