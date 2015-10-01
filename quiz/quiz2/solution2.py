for i in range(1, 101):
    res = i
    if i % 3 == 0:
        res = 'Fuzz'
        if i % 5 == 0:
            res += 'Buzz'
    elif i % 5 == 0:
        res = 'Buzz'
    print(res)
