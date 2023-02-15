points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    sum = 0

    if coordinates == [] or len(coordinates) == 1:
        return 0

    for index, val in enumerate(coordinates):

        if index + 1 != len(coordinates):

            if coordinates[index] < coordinates[index + 1]:

                tups = (coordinates[index], coordinates[index + 1])

                for k, v in points.items():
                    if tups == k:
                        sum += v

            else:

                tups = (coordinates[index + 1], coordinates[index])

                for k, v in points.items():
                    if tups == k:
                        sum += v
        else:
            return sum

    return sum


calculate_distance([0, 1, 3])
