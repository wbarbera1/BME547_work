# Calculate Coordinates

def calculate_value():
    x_coord1 = int(input("X1: "))
    y_coord1 = int(input("Y1: "))
    x_coord2 = int(input("X2: "))
    y_coord2 = int(input("Y2: "))
    x_val = int(input("Enter an x-value: "))
    coord1, coord2 = input_coordinates(x_coord1, x_coord2, y_coord1, y_coord2)
    slope = calc_slope(coord1, coord2)
    interc = calc_intercept(coord1, coord2, slope)
    y_value = y_coord_out(slope, interc, x_val)
    print("Corresponding y_value = {}".format(y_value))


def input_coordinates(x_coord1, x_coord2, y_coord1, y_coord2):
    coord1 = (x_coord1, y_coord1)
    coord2 = (x_coord2, y_coord2)
    return coord1, coord2


def calc_slope(coord1, coord2):
    slope = (coord2[1] - coord1[1])/(coord2[0] - coord1[0])
    return slope


def calc_intercept(coord1, coord2, slope):
    interc = coord1[1] - slope*coord1[0]
    return interc


def y_coord_out(slope, interc, x_val):
    y_value = slope*x_val + interc
    return y_value


if __name__ == "__main__":
    calculate_value()
