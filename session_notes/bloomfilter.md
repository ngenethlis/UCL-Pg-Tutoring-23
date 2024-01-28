# Bloom Filters

## Problem:
- Is element a in Set A?

## Bloom Filter is a probabilistic data structure based on hashing, used to solve this problem
- It can tell whether an element is **definitely not** in a set or **possibly** in a set

## How does it work?
Init:
- It uses a bit array of size m, initialized with all 0s
- It uses k hash functions
- It uses a set of n elements

Insert an element x:
- For each hash function, hash x to a value between 0 and m-1
- Set the corresponding bit (to each hash function) to 1

Search for an element x:
- For each hash function, hash x to a value between 0 and m-1
- If any of the corresponding bits is 0, then x is **definitely not** in the set
- If all of the corresponding bits is 1, then x is **possibly** in the set


## Summary:

Bloom Filter, similar to hashmap but instead of storing (key:value) pairs, we mark the key position as 1 (filled)
Many keys might map to the same position, so we might have false positives
But we will never have false negatives (i.e x is in the set but query returns false), because if x is in the set, all the bits corresponding to x will be 1.
Because of this, we can use bloom filters to check if an element is **possibly** in a set, and if yes we can do a more expensive check, with other data structures to see if it is **definitely** in the set.
A bloom filter is extremely efficient in both time and space usage. These features are so important that it gives up accuracy to maintain them.

Space complexity: O(m)
Time complexity: O(k) for *both* insert and search


### How to choose m and k and which hash functions?
- m: size of the bit array
- k: number of hash functions
- n: number of elements in the set
- p: false positive probability
- Generally want fast computation and uniform distribution
- Murmur3 good tradeoff between speed and uniform distribution
- Cryptographic hash functions have uniform distribution
- - [Extra reading, "better bloom filter"](https://www.eecs.harvard.edu/~michaelm/postscripts/tr-02-05.pdf)
hash_i = hash1+ i*hash2
- So we can use mmh3 as hash1 and sha256 as hash2

Through some [math](https://brilliant.org/wiki/bloom-filter/#properties), we can derive the following:

- Optimal number of hash functions: k = (m/n)ln2
- Optimal size of bit array: m = -n(lnp) / (ln2)^2
- p = (1 - e^(-kn/m))^k


## Now you know how to use a bloom filter, but how do you implement it?