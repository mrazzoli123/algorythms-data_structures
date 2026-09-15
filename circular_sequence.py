class CircularSequence:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.n = 0
        self.f = 0
        self.l = 0

    def rank2index(self, rank):
        return (self.f + rank) % self.capacity

    def index2rank(self, index):
        return (self.capacity - self.f + index) % self.capacity

    def elemAtRank(self, rank):
        if rank < 0 or rank >= self.n:
            raise IndexError("Rank out of bounds")
        index = self.rank2index(rank)
        return self.array[index]

    def size(self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def insertLast(self, element):
        if self.size() == self.capacity - 1:
            raise Exception("Sequence is full")
        self.array[self.l] = element
        self.l = (self.l + 1) % self.capacity
        self.n += 1

    def insertFirst(self, element):
        if self.size() == self.capacity - 1:
            raise Exception("Sequence is full")
        self.f = (self.capacity + self.f - 1) % self.capacity
        self.array[self.f] = element
        self.n += 1

    def insertAtRank(self, rank, element):
        if rank < 0 or rank > self.n:
            raise IndexError("Rank out of bounds")
        if self.size() == self.capacity - 1:
            raise Exception("Sequence is full")

        if rank == 0:
            self.insertFirst(element)
        elif rank == self.n:
            self.insertLast(element)
        else:
            index = self.rank2index(rank)
            if rank < self.n // 2:
                self.f = (self.f - 1 + self.capacity) % self.capacity
                for i in range(0, rank):
                    self.array[self.rank2index(i)] = self.array[self.rank2index(i + 1)]
            else:
                for i in range(self.n, rank, -1):
                    self.array[self.rank2index(i)] = self.array[self.rank2index(i - 1)]
                self.l = (self.l + 1) % self.capacity
            self.array[index] = element
            self.n += 1

    def removeAtRank(self, rank):
        if rank < 0 or rank >= self.n:
            raise IndexError("Rank out of bounds")

        index = self.rank2index(rank)
        removed_element = self.array[index]

        if rank < self.n // 2:
            for i in range(rank, 0, -1):
                self.array[self.rank2index(i)] = self.array[self.rank2index(i - 1)]
            self.f = (self.f + 1) % self.capacity
        else:
            for i in range(rank, self.n - 1):
                self.array[self.rank2index(i)] = self.array[self.rank2index(i + 1)]
            self.l = (self.l - 1 + self.capacity) % self.capacity

        self.n -= 1
        return removed_element


sequence = CircularSequence(10)

sequence.insertFirst(10)
sequence.insertLast(20)
sequence.insertLast(30)

sequence.insertAtRank(1, 15)

print("Sequence after insertion:", [sequence.elemAtRank(i) for i in range(sequence.size())])

removed = sequence.removeAtRank(1)
print(f"Removed element: {removed}")

print("Sequence after removal:", [sequence.elemAtRank(i) for i in range(sequence.size())])
