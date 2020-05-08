def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for key, value in enumerate(weights):
        if value in cache:
            cache[value].append(key)
        else:
            cache[value] = [key]

    for value in cache:
        if limit - value in cache:
            if cache[limit - value] is cache[value]:
                if len(cache[value]) >= 2:
                    return (cache[limit - value][1], cache[value][0])
            else:
                return (cache[limit - value][0], cache[value][0])

    return None


print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
