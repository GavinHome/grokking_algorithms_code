def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    start, end, count = 0, 0, 0
    sets = set()
    sets.add(s[start:end+1])
    while start < len(s) and end < len(s):
        # print("sets", sets)
        if len(sets) == end - start + 1:
            count = max(count, end - start + 1)

            end += 1
            if end < len(s):
                sets.add(s[end])
                # print("end+1", sets)
        else:
            if start < len(s) and s[start] != s[end]:
                sets.discard(s[start])
                # print("start+1", sets)
            start += 1
    print("sets", sets)
    return count

print(lengthOfLongestSubstring("aab"))
# print(lengthOfLongestSubstring("pwwkew"))