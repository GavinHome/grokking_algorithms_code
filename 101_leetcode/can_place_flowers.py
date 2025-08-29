def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    # temp = [0] + flowerbed + [0]
    # print("temp:", temp)
    # move = 1
    # count = 0
    # while move <= len(flowerbed):
    #     if temp[move] == 1:
    #         move += 2
    #         continue

    #     if temp[move] == 0 and temp[move-1] == 0 and temp[move+1] == 0:
    #         count += 1
    #         print("move:", move)
    #         move += 2
    #     elif flowerbed[move-1] == 1:
    #         move += 1
    #     elif flowerbed[move+1] == 1:
    #         move += 2
        
    #     if count == n:
    #         break

    # return count == n

    # if n == 0:
    #     return True
    
    # for i in range(len(flowerbed)):
    #     if flowerbed[i] == 0:
    #         left_ok = i == 0 or flowerbed[i-1] == 0
    #         right_ok = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

    #         if left_ok and right_ok:
    #             # flowerbed[i] = 1
    #             i += 2
    #             n -= 1
    #             if n <= 0:
    #                 return True
    
    # return False

    if n == 0:
        return True
    
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
    
    return n <= 0

print(canPlaceFlowers([1,0,0,0,1,0,0], 2))
