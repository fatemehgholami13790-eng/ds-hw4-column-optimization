
from collections import defaultdict

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, x, y):
        return (x * 31 + y) % self.size

    def insert(self, x, y, z, index):
        index_ = self._hash(x, y)
        self.table[index_].append((x, y, z, index))

    def search(self, x, y):
        index_ = self._hash(x, y)
        return self.table[index_]

def solve():
    N = int(input())
    hash_table = HashTable(100)
    blocks = []

    for i in range(N):
        x, y, z = map(int, input().split())
        x, y = max(x, y), min(x, y)
        blocks.append((x, y, z, i + 1))
        hash_table.insert(x, y, z, i + 1)

    max_height = 0
    best_stack = []

    # گروه‌بندی بلوک‌ها بر اساس پایه
    groups = defaultdict(list)
    for x, y, z, idx in blocks:
        groups[(x, y)].append((z, idx))

    for base, items in groups.items():
        # مرتب‌سازی ارتفاع‌ها نزولی
        items.sort(reverse=True)
        current_height = 0
        current_stack = []
        for z, idx in items:
            current_height += z
            current_stack.append(idx)
            if current_height > max_height:
                max_height = current_height
                best_stack = current_stack.copy()

    print(len(best_stack))
    print(" ".join(map(str, sorted(best_stack))))
    print(max_height)

if __name__ == "__main__":
    solve()
