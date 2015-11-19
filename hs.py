def hs(n):
    l = 0
    while (n != 1):
        l = l + 1
        print (n)
        if (n % 2 == 0):
            n = (n//2)
        else:
            n = (3 * n + 1)
    print (n)
    print (l + 1)
    return None
