from datetime import datetime, timedelta


def solve(n, x, y):
    return n*x + n*y - (2*x*y)

def print_result(n, x, y, result):
    print(f"n: {n}, x: {x}, y: {y}, result: {result}")

def times_up(start):
    return start < datetime.now() - timedelta(minutes=1)

def main():
    start = datetime.now()
    checked = set()
    for n in range(0, 5000):
        min_result_for_n = None
        if n % 2 == 1:
            print(n)
            for x in range(0, n+1):
                if x % 2 == 0:
                    for y in range(0, n+1):
                        if y % 2 == 1:
                            if (x, y) not in checked:
                                result = solve(n, x, y)
                                if min_result_for_n is None or result < min_result_for_n:
                                    min_result_for_n = result
                                if result == 1:
                                    print("Solution found:")
                                    print_result(n, x, y, result)
                                    return
                                checked.add((x, y))
            print(f"Min Result: {min_result_for_n}")
        if times_up(start):
            print("Timeout")
            return


if __name__ == "__main__":
    main()
