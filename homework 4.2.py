tests = [
    [0, 1, 7, 2, 4, 8, 11, 5],
    [1, 4, 7, 9, 3, 10],
    [7, 8, 4, 9, 2, 11, 12, 5],
]

for a in tests:
    result = (sum(a[::2]) * a[-1]) if a else 0
    print(result)
