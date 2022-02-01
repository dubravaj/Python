import math

if __name__ == "__main__":

    # lambda expression - anonymous function
    reverse = lambda x: x[::-1]
    descend = lambda x: reverse(sorted(x))

    example_string = "redro esreveR"
    values = [1, 2, 6, 4, 3, 7, 48, 22]
    print(reverse(example_string))
    print(descend(values))

    # vector length calculator using map
    coordinates_X = (0, 0)
    coordinates_Y = (3, 5)
    coordinates_XY = zip(coordinates_X, coordinates_Y)
    diff_pow = lambda p: (p[0] - p[1]) ** 2
    vector_length = math.sqrt(sum(map(diff_pow, coordinates_XY)))
    print(vector_length)

    sum_two = lambda x, y: x + y
    # map with multiple iterables
    f = map(sum_two, [1, 2, 3, 5], [2, 5, 6, 9])
    print(list(f))

    # filter routes longer than 30 km
    routes = [
        {"length": 24.6, "name": "Route 41"},
        {"length": 150.6, "name": "Route 42"},
        {"length": 45.2, "name": "Route 43"},
        {"length": 29.3, "name": "Route 44"},
    ]
    routes = list(filter(lambda row: row["length"] > 30, routes))
    print(routes)
