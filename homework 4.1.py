tests = [
    [0, 5, 7, 0, 0, 4, 0, 12, 3],
    [0, 4, 1, 6, 8, 0, 0, 2],
    [0, 0, 11, 0, 13, 0, 15, 10],
    [8, 6, 0, 0, 0, 0, 0, 5, 45, 0, 0, 6],
]

for lst in tests:
    nonzeros = [x for x in lst if x != 0]
    result = nonzeros + [0] * (len(lst) - len(nonzeros))
    print(f"{lst} -> {result}")