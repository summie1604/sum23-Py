

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    prev_results = {}
    while True:
        number = int(input("Enter a number: "))
        if number in prev_results:
            print("Already computed. Returning the same...")
            result = prev_results[number]
        else:
            result = fib(number)
            prev_results[number] = result
        print(result)
