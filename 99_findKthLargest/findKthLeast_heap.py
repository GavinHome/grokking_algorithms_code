import heapq

# hp = [2,3,1]
# heapq.heapify(hp)

# print(hp)

def inventoryManagement(stock, cnt):
    if cnt == 0:
        return list()

    hp = [-x for x in stock[:cnt]]
    heapq.heapify(hp)
    print("init hp", hp)
    for i in range(cnt, len(stock)):
        if -hp[0] > stock[i]:
            print("for -hp[0]", -hp[0])
            heapq.heappop(hp)
            print("for heappop", hp)
            heapq.heappush(hp, -stock[i])
            print("for heappush", hp)
    print("end hp", hp)
    ans = [-x for x in hp]
    print("ans", hp)
    return ans


print(inventoryManagement([1,-3,-2,-6,-111],3))

