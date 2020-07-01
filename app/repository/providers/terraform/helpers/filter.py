def filtering(result, cmp):
    result = list(filter(lambda x: rule(x, cmp), result))
    result = list(map(lambda x: x.get('instances'), result))
    result = sum(result, [])
    return result


def rule(obj, filts):
    for key, value in filts.items():
        return obj.get(key) in value
