def pi(distance):
    x = 0.0
    y = 0.0

    total = 0
    circle = 0

    while y < 1:
        if x >= 1:
            total += 1
            y += distance
            x = 0

        if x != 1:
            total += 1
            x += distance

        if (x*y + y*y) <= 1:
            circle += 1

        print(total)
        print(circle)
        print(4*(float(circle)/float(total)))

    return 4*(float(circle)/float(total))


print(pi(.0000001))
