def hs1(n):
    count = 0
    while (n != 1):
        print(n)
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        count = count + 1
    print(1)
    print(count)
    return None 
