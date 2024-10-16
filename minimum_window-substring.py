# Abu Kamal
# two string 's' and 't'
# find minimum substring of s that has element of t
# initiate two dict and compare dictT with dictS
#



def minimumwindow_substring(s, t):
    # edge case
    if len(s) < len(t):
        return ""
    # define two dict to get count of t and sliding window
    countT, window = {}, {}
    for c in t:    # find need
        countT[c] = 1 + countT.get(c, 0)
    have, need = 0, len(countT)
    res = [-1, -1]
    resLen = float('infinity')

    left = 0
    for right in range(len(s)):  # add char of s to dict with right pointer
        c = s[right]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            if (right - left + 1) < resLen:
                res = [left, right]
                resLen = (right - left + 1)
            window[s[left]] -= 1
            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            left += 1
    left, right = res
    return s[left:right+1] if resLen != float('infinity') else ""


print(minimumwindow_substring("ADOBECODEBANC", "ABC"))
