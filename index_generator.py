if __name__ == '__main__':
    indexes = list(input('Columns(space separated): ').strip().split(' '))
    subsets = []
    n = len(indexes)

    max_indexes = 2**n

    for i in range(max_indexes):
        subset = []
        for j in range(n):
            if i & (1 << j) > 0:
                subset.append(indexes[j])
        subsets.append(subset)
    subsets.sort(key = len)
    
    for i in range(max_indexes - 1, -1, -1):
        for j in range(i):
            if subsets[j] == -1 or subsets[i] == -1:
                continue
            if subsets[j] == subsets[i][:len(subsets[j])]:
                subsets[j] = -1
    result =  []
    for subset in subsets:
        if subset != -1:
            result.append(subset)

    print(len(result), 'indexes')
    for index in result:
        print(', '.join(index))

