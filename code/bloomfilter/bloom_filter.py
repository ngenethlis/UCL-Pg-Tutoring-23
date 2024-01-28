import hashlib
import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size, k=3):
        hashF = [
            lambda x: mmh3.hash(x, 0),
            lambda x: hashlib.sha256(str(x).encode()).digest().__hash__()
        ]
        pass

    def add(self, element):
        pass

    def __contains__(self, element):
        pass

    def __len__(self):
        pass
