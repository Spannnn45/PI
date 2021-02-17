def pi(distance):
    x = 0.0
    y = 0.0

    total = 0
    circle = 0

    while y < 1:
        print(x, y)
        if x >= 1:
            total += 1
            y += distance
            x = 0

        if x != 1:
            total += 1
            x += distance

        if (x*y + y*y) <= 1:
            circle += 1

    return 4*(circle/total)


print(pi(.001))
