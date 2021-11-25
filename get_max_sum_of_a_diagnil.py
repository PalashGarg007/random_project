'''Max sum of a diagnol in a m*n matrix'''


def getmaxdiagnol(m, n, arr):
    possibility = []

    for i in range(m):
        sum = 0
        b = 0
        for a in range(i, m):
            sum += arr[a][b]
            if (a == m-1) or (b == n-1):
                break
            b += 1
        possibility.append(sum)

    for j in range(1, n):
        sum = 0
        b = j
        for a in range(m):
            sum += arr[a][b]
            if (a == m-1) or (b == n-1):
                break
            b += 1
        possibility.append(sum)

    for i in range(m):
        sum = 0
        b = 0
        for a in range(i, -1, -1):
            sum += arr[a][b]
            if (a == 0) or (b == n-1):
                break
            b += 1
        possibility.append(sum)

    for j in range(1, n):
        sum = 0
        b = j
        for a in range(m-1, -1, -1):
            sum += arr[a][b]
            if (a == 0) or (b == n-1):
                break
            b += 1
        possibility.append(sum)

    return max(possibility)


print(getmaxdiagnol(3, 4, [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1]]))
