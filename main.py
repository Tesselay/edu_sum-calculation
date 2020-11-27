def sum_iterative(n):

    sum = 0
    for i in range(0, n + 1):
        sum += i

    return sum


def sum_recursion(n):
    if n == 0:
        return n
    else:
        return n + sum_recursion(n-1)


if __name__ == '__main__':
    print(sum_iterative(5))
    print(sum_recursion(3))

