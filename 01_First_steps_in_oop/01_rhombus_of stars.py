def row_print(row, size):
    for space in range(size - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=" ")
    print("*")


def rhombus_top_part(size):
    for row in range(1, size + 1):
        row_print(row, size)


def rhombus_bottom_part(size):
    for row in range(size - 1, 0, -1):
        row_print(row, size)


def print_rhombus(size):
    rhombus_top_part(size)
    rhombus_bottom_part(size)


print_rhombus(int(input()))
