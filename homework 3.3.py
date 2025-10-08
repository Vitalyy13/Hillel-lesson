lst = [1, 2, 3, 4, 5, 6, 7]

if not lst:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]
print(result)





