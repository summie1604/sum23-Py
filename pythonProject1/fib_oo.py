class Fib:
    cache = {}

    @classmethod
    def get(cls, n):
        # same logic as before
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cls.cache:
            print(f"Fib({n}) already in cache")
            return cls.cache[n]
        res = Fib.get(n - 1) + Fib.get(n - 2)
        cls.cache[n] = res
        return res


if __name__ == "__main__":
    while True:
        number = int(input("Enter a number: "))
        result = Fib.get(number)
        print(result)