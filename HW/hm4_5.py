def lookup_key(data, value):
    k = []
    for key, val in data.items():
        if value == val:
            k.append(key)
    return k


data = {
    "F": 1,
    "FX": 2,
    "E": 3,
    "D": 3,
    "C": 4,
    "B": 5,
    "A": 5,
}
lookup_key(data, "okiu")
