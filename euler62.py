x = 1
origins = dict()
while x < 10000:
    x += 1
    origin = tuple(sorted(str(x ** 3)))
    if origin in origins:
        origin_list = origins[origin]
        origin_list.add(x)
        if len(origin_list) >= 5:
            print(origin_list)
            print(origin)
            print(min(origin_list) ** 3)
            break
    else:
        origins[origin] = {x}
