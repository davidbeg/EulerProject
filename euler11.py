import textwrap

GRID_SIZE = 20
SEQUENEC_SIZE = 4
number = textwrap.wrap('''\
0802229738150040007504050778521250779108\
4949994017811857608717409843694804566200\
8149317355791429937140675388300349133665\
5270952304601142692468560132567137023691\
2231167151676389419236542240402866331380\
2447326099034502447533537836842035171250\
3298812864236710263840675954706618386470\
6726206802621220956394396308409166499421\
2455580566739926971778789683148834896372\
2136230975007644204535140061339734313395\
7817532822753167159403800462161409535692\
1639054296353147555888240017542436298557\
8656004835718907054444374460215851541758\
1980816805944769287392138652177704895540\
0452088397359916079757321626267933279866\
8836688757622072034633674655123263935369\
0442167338253911249472180846293240627636\
2069364172302388346299698267598574043616\
2073352978319001743149714886811623570554\
0170547183515469169233486143520189196748\
''', GRID_SIZE * 2)

largest_product = 0


def get_cell(i, j):
    return int(number[i][j * 2:][:2])


def get_products(i, j):
    products = []
    # clac 4 to the right
    if j <= GRID_SIZE - SEQUENEC_SIZE:
        products.append(1)
        for index in range (j, j + SEQUENEC_SIZE):
            products[-1] *= get_cell(i, index)
        if i <= GRID_SIZE - SEQUENEC_SIZE:
            products.append(1)
            for offset in range(0, SEQUENEC_SIZE):
                products[-1] *= get_cell(i + offset, j + offset)
    # clac 4 down
    if i <= GRID_SIZE - SEQUENEC_SIZE:
        products.append(1)
        for index in range(i, i + SEQUENEC_SIZE):
            products[-1] *= get_cell(index, j)
        if SEQUENEC_SIZE - 1 <= j:
            products.append(1)
            for offset in range(0, SEQUENEC_SIZE):
                products[-1] *= get_cell(i + offset, j - offset)
    return products


for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        products = get_products(i, j)
        largest_product = max(products + [largest_product])
print(largest_product)
