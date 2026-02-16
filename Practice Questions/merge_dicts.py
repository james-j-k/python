def merge_dicts(d1, d2):
    result = {}

    # Add all keys from d1
    for key in d1:
        result[key] = d1[key]

    # Merge values from d2
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]

    return result
    
d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}

print(merge_dicts(d1, d2))
