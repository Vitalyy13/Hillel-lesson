lst = [15, 6, 2, 7, 1, 13]

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)