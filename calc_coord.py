# Calculate Coordinates

def calculate_value():
    coord1, coord2 = input_coordinates()
    slope = calc_slope(coord1, coord2)
    y_value = y_coord_out(slope, 5)
    print(y_value)

def input_coordinates():
    coord1 = (0, 0)
    coord2 = (2, 1)
    return coord1, coord2

def calc_slope(coord1, coord2):
    slope = (coord2[1] - coord1[1])/(coord2[0] - coord1[0])
    return slope

def y_coord_out(slope, x_val)
    y_value = slope*x_val
    return y_value

if __name__ == "__main__"
    calculate_value()

