def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        for j in range(n):
            nums1[j] = nums2[j]
        return
    temp_nums1 = [x for x in nums1[:m]]        
    i,j = 0,0
    idx = 0
    while i < m and j < n:
        if temp_nums1[i] <= nums2[j]:
            nums1[idx] = temp_nums1[i]
            i += 1
        else:
            nums1[idx] = nums2[j]
            j += 1
        idx += 1
    
    if i < m:
        while i < m:
            nums1[idx] = temp_nums1[i]
            i += 1
            idx += 1
    
    if j < n:
        while j < n:
            nums1[idx] = nums2[j]
            j += 1
            idx += 1
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, 3, nums2, n)
print(nums1)

