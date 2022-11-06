def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    table = [0, 1, 1]

    for i in range(3, n + 1):
        table.append(table[i - 1] + table[i - 2])

    return table[n]

    # Write your code here.


n = int(input())
print(fibonacci(n))
