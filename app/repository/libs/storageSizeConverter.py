
def multiple_ten(size, stype):
    arr = {
        'MB': 0.001,
        'TB': 1000,
        'PB': 1000000
    }

    return size * arr.get(stype, 1)