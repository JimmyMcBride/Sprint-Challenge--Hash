def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for i in range(len(weights)):
        if weights[i] > limit:
            pass
        else:
            if weights[i] not in cache:
                cache[i] = weights[i]
            for key, value in enumerate(weights):
                if key == i or value > limit:
                    pass
                else:
                    my_sum = cache[i] + value
                    print(
                        f"my sum: cache[i] ({cache[i]}) + value ({value}) = {cache[i] + value}"
                    )
                    if my_sum == limit:
                        print(f"{(key, i)}")
                        return (key, i)

    return None


# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
