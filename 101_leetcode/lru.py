class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """      
        self.capacity = capacity
        self.sets = {}
        self.queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.sets:
            return -1
        
        self.queue.remove(key)
        self.queue.append(key)
        return self.sets[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.sets:
            self.sets[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            self.sets[key] = value
            self.queue.append(key)

        if len(self.sets) > self.capacity:
            self.sets.pop(self.queue[0])
            self.queue.pop(0)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1); # 缓存是 {1=1}
# lRUCache.put(2, 2); # 缓存是 {1=1, 2=2}
# print(lRUCache.get(1));    # 返回 1
# lRUCache.put(3, 3); # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# print(lRUCache.get(2));    # 返回 -1 (未找到)
# lRUCache.put(4, 4); # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# print(lRUCache.get(1));    # 返回 -1 (未找到)
# print(lRUCache.get(3));    # 返回 3
# print(lRUCache.get(4));    # 返回 4


lRUCache = LRUCache(1)
lRUCache.put(2, 1); # 缓存是 {2=1}
print(lRUCache.get(2));    # 返回 1
lRUCache.put(3, 2); # 该操作会使得关键字 2 作废，缓存是 {3=2}
print(lRUCache.get(2));    # 返回 -1 (未找到)
print(lRUCache.get(3));    # 返回 2

["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]