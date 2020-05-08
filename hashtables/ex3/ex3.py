def intersection(arrays):
    result = []
    cache = {}

    for arr in arrays:
        for key, value in enumerate(arr):
            print(key, value)
            if value not in cache:
                cache[value] = key

    return result


print(intersection([[1, 2, 3], [1, 4, 5, 3], [1, 6, 7, 3]]))

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(arrays)

#     print(intersection(arrays))
