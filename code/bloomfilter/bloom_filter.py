import hashlib
import mmh3


class BloomFilter:
    def __init__(self, size, k=2):
        self.size = size
        self.k = k
        self.hashF = self._generateHashFuns()
        self.bitArray = [0] * self.size

    def add(self, element):
        for h in self.hashF:
            self.bitArray[h(element) % self.size] = 1

    def __contains__(self, element):
        all1 = 1
        for h in self.hashF:
            all1 = all1 and self.bitArray[h(element) % self.size]
        return all1 == 1

    def __len__(self):
        pass

    def _generateHashFuns(self):
        hashF= [lambda x : mmh3.hash(x,0),
                lambda x : hash(x)]
        for i in range(2,self.k):
            hashF.append(lambda x: hashF[0](x)+i*hashF[1](x))
        return hashF



def main():
    bf = BloomFilter(100,6)
    elems = ['apple', 'banana', 'potato', 'strawberry']
    for e in elems:
        bf.add(e)

    elemsToSearch = ['apple','kumquat','mandarin','cantonese','sweet and sour pork im hungy',
                     'banana','potato','strawberry','pineapple','orange','pear','grape','watermelon'
                      'mango','kiwi','peach']
    for e in elemsToSearch:
        r = e in bf
        print(f"{e} in bf is {r}")




main()