"""
Sorting Iterables
"""

import random

random.seed(0) # with this we have always the same number when we re-run
# seed makes sure we keep the same sequence of pseudo-random numbers
for _ in range(10):
    print(random.randint(1,10))


class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self.length = length
        self.seed = seed
        self.lower = lower
        self.upper = upper

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.RandomIterator(self.length,
                                   seed = self.seed,
                                   lower=self.lower,
                                   upper=self.upper)

    class RandomIterator:
        def __init__(self, length, *, seed, lower, upper):
            self.length = length
            self.lower = lower
            self.upper = upper
            self.num_requests = 0
            random.seed(seed) # reset the seed every time the iterator is created

        def __iter__(self):
            return self

        def __next__(self):
            if self.num_requests >= self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)
                self.num_requests += 1
                return result

print("=======")
randoms = RandomInts(10)
#randoms = RandomInts(10, seed=None) # if we want different numbers
for num in randoms:
    print(num)
print(list(randoms))
print(sorted(randoms)) # soted works for iterables in general not just sequence types
print(sorted(randoms,reverse=True))
