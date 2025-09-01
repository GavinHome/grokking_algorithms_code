from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.cnt = {}    # key -> freq
        self.freq = defaultdict(OrderedDict)  # freq -> keys in insertion order
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        self._update_freq(key)
        return self.cache[key]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self._update_freq(key)
        else:
            if len(self.cache) >= self.capacity:
                # 淘汰最少访问次数且最早插入的 key
                remove_key, _ = self.freq[self.min_freq].popitem(last=False)
                del self.cache[remove_key]
                del self.cnt[remove_key]
            self.cache[key] = value
            self.cnt[key] = 1
            self.freq[1][key] = None
            self.min_freq = 1

    def _update_freq(self, key):
        freq = self.cnt[key]
        # 从旧频率组删除
        del self.freq[freq][key]
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        # 加入新频率组
        self.cnt[key] += 1
        self.freq[self.cnt[key]][key] = None


def printLFU(tag, lfu):
    print(tag, "cnt=", lfu.cnt, "cache=", lfu.cache)

def printGet(tag, value):
    print(tag, value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cnt(x) = 键 x 的使用计数
# cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）

# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
# [null,null,null,  1, null, -1,  3,  null, -1, 3,  4]

# lfu = LFUCache(2)

# lfu.put(1, 1);      # cache=[1,_], cnt(1)=1
# printLFU("put(1)", lfu)
# lfu.put(2, 2);      # cache=[2,1], cnt(2)=1, cnt(1)=1
# printLFU("put(2)", lfu)
# print(lfu.get(1));  # 返回 1
#                     # cache=[1,2], cnt(2)=1, cnt(1)=2
# printLFU("get(1)", lfu)
# lfu.put(3, 3);      # 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                     # cache=[3,1], cnt(3)=1, cnt(1)=2
# printLFU("put(3)", lfu)
# print(lfu.get(2));  # 返回 -1（未找到）
# print(lfu.get(3));  # 返回 3
#                     # cache=[3,1], cnt(3)=2, cnt(1)=2
# printLFU("get(3)", lfu)        
# lfu.put(4, 4);      # 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                     # cache=[4,3], cnt(4)=1, cnt(3)=2
# printLFU("put(4)", lfu)
# print(lfu.get(1));  # 返回 -1（未找到）
# print(lfu.get(3));  # 返回 3
#                     # cache=[3,4], cnt(4)=1, cnt(3)=3
# printLFU("get(3)", lfu)
# print(lfu.get(4));  # 返回 4
#                     # cache=[3,4], cnt(4)=2, cnt(3)=3
# printLFU("get(4)", lfu)


# ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
# [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# [null,null,null,  2,  1,  2,  null, null, -1, 2,  1,  4]
# lfu = LFUCache(3)
# lfu.put(2, 2);
# printLFU("put(2,2)", lfu)
# lfu.put(1, 1);
# printLFU("put(1, 1)",lfu)
# print(lfu.get(2));
# printLFU("get(2)",lfu)
# print(lfu.get(1));
# printLFU("get(1)",lfu)
# print(lfu.get(2));
# printLFU("get(2)",lfu)
# lfu.put(3, 3);
# printLFU("put(3, 3)",lfu)
# lfu.put(4, 4);
# printLFU("put(4, 4)",lfu)
# print(lfu.get(3));
# printLFU("get(3)",lfu)
# print(lfu.get(2));
# printLFU("get(2)",lfu)
# print(lfu.get(1));
# printLFU("get(1)",lfu)
# print(lfu.get(4));
# printLFU("get(4)",lfu)


# ["LFUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# [null,-1,null,-1,null,null,2,6]
lfu = LFUCache(2)
printGet("get(2)", lfu.get(2))
lfu.put(2, 6)
printLFU("put(2)", lfu)
printGet("get(1)", lfu.get(1))
lfu.put(1, 5)
printLFU("put(1)", lfu)
lfu.put(1, 2)
printLFU("put(1)", lfu)
printGet("get(1)", lfu.get(1))
printGet("get(2)", lfu.get(2))