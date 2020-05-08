def has_negatives(a):
    balance = []
    dark_side = {}
    light_side = {}

    for num in a:
        if num < 0:
            dark_side[num] = num * -1
        elif num > 0:
            light_side[num] = num

    for num in dark_side.values():
        if num in light_side:
            balance.append(light_side[num])

    return balance


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
