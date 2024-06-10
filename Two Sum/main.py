def find_incexes(a, b):
    indexes = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == b:
                indexes.append(i)
                indexes.append(j)
    return indexes


a = [2, 7, 11, 15]
b = 9
result = find_incexes(a, b)
print(result)