lst = [6, 1, 9, 56, 2, 99, 13]

if not lst:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]
print(result)





