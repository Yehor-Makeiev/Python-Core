def prepare_data(data):
    max = data[0]
    min = data[0]
    for i in data:
        if i > max:
            max = i
        elif i < min:
            min = i
    data.pop(data.index(max))
    data.pop(data.index(min))
    data.sort()
    return data


data = [1, -3, 4, 100, 0, -5, 10, 1, 1]
print(prepare_data(data))
