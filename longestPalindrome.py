def longestPalindrome(s):
    if len(s) < 2:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        print("loop i: ", i, s[i:i+1])
        left1, right1 = expand(s, i, i)
        left2, right2 = expand(s, i, i+1)

        if right1 - left1 > end - start:
            start, end = left1, right1

        if right2 - left2 > end - start:
            start, end = left2, right2
        
    return s[start:end+1]

def expand(s, left, right):
    print("expand: ", s[left:right+1])
    while left >=0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return left + 1, right - 1


print(longestPalindrome("aabbaa"))
       