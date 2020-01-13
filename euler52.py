for i in range(4, 20):
    for num in range(10 ** i, int((1.0/6) * 10 ** (i + 1) + 1)):
        products = [num * j for j in range(2, 7)]
        are_similar = map(lambda x: sorted(str(x)) == sorted(str(num)), products)
        if all(are_similar):
            print(num, [num * j for j in range(2, 7)])
            exit()
