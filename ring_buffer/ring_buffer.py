class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.capacity > self.current:
            self.storage.pop(0)
            self.storage.append(item)
            self.current += 1

        elif self.capacity == self.current:
            self.storage.pop(0)
            self.storage.insert(0, item)
            self.current += 1
        else:
            self.storage.pop(self.current - self.capacity)
            self.storage.insert(self.current - self.capacity, item)
            self.current += 1

    def get(self):
        storage = self.storage
        storage = [x for x in storage if x is not None]
        return storage

# THIS FAILS AFTER IT REACHES 2 loops in!
# buf = RingBuffer(4)


# buf.append(1)
# print(buf.get())
# buf.append(1)
# print(buf.get())
# buf.append(3)
# print(buf.get())
# buf.append(7)
# print(buf.get())
# buf.append(10)
# print(buf.get())
# buf.append(9)
# print(buf.get())
# buf.append(3)
# print(buf.get())
# buf.append(6)
# print(buf.get())
# buf.append(2)
# print(buf.get())
# buf.append(5)
# print(buf.get())
# buf.append(6)
