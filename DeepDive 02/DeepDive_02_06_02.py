from functools import lru_cache


class Fib:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, s):
        if isinstance(s, int):
            # single item requested
            if s < 0:
                s = self._n + s
            if s < 0 or s > self._n - 1:
                raise IndexError
            return self._fib(s)
        else:
            # slice being requested
            idx = s.indices(self._n)
            rng = range(idx[0], idx[1], idx[2])
            return [self._fib(n) for n in rng]

    @staticmethod
    @lru_cache(2 ** 32)
    def _fib(n):
        if n == 0: return 1
        else:
            i, j = 1, 2
            for index in range(1, n):
                i, j = j, i+j
        return i


myfib = Fib(10)
for i in range(10):
    print(i, ":", myfib[i])
myfib[-1]
print(myfib[5:8])