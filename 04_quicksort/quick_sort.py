
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        left = [x for x in nums[1:] if x <= pivot]
        right = [x for x in nums[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
# print([2,1,3] + [5,4,6])
print(quick_sort([3,3,-1,-2]))