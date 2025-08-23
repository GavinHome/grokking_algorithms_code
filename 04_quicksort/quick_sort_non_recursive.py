
def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j], arr[i]
    
    arr[i+1],arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        stack = [(0, len(nums) -1)]

        while stack:
            low, high = stack.pop()
            if low >= high: continue
            pivot_idx = partition(nums, low, high)

            if pivot_idx + 1 < high:
                stack.append((pivot_idx + 1, high))
            
            if pivot_idx - 1 > low:
                stack.append((low, pivot_idx - 1))
        return nums

print(quick_sort([5,1,1,2,0,0]))