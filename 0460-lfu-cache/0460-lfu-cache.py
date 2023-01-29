class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.count = collections.defaultdict(int)
        self.buckets = collections.defaultdict(set)
        self.buckets_by_recency = collections.defaultdict(collections.deque)
        self.min = 10 ** 20

    def increment(self, key: int):
        self.buckets[self.count[key]].remove(key)
        if self.min == self.count[key] and len(self.buckets[self.count[key]]) == 0:
            self.min += 1
        self.count[key] += 1
        if self.min > self.count[key]:
            self.min = self.count[key]
        self.buckets[self.count[key]].add(key)
        self.buckets_by_recency[self.count[key]].append(key)

    def get(self, key: int) -> int:
        if key in self.dict:
            self.increment(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if len(self.dict) == self.capacity and key not in self.dict:
            while len(self.buckets[self.min]) == 0:
                self.min += 1

            pkey = self.buckets_by_recency[self.min].popleft()
            while pkey not in self.buckets[self.min]:
                pkey = self.buckets_by_recency[self.min].popleft()

            self.buckets[self.min].remove(pkey)
            del self.dict[pkey]
            del self.count[pkey]

        if key not in self.dict:
            self.min = 1
            self.count[key] = 1
            self.dict[key] = value
            self.buckets[1].add(key)
            self.buckets_by_recency[1].append(key)
            return

        self.dict[key] = value
        self.increment(key)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)