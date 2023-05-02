
# matrix-manipulator.py (Row Operations)
# Push-up count: 40

from fractions import Fraction


def swap_rows(matrix, row_x, row_y):
    matrix[row_x], matrix[row_y] = matrix[row_y], matrix[row_x]
    print_matrix(matrix)
    return matrix


def scale_row(matrix, row_x, constant):
    for i in range(len(matrix[row_x])):
        matrix[row_x][i] *= constant
    print_matrix(matrix)
    return matrix


def add_row(matrix, row_to_modify, row_y, constant):
    for i in range(len(matrix[row_y])):
        matrix[row_to_modify][i] += matrix[row_y][i] * constant
    print_matrix(matrix)
    return matrix


def subtract_row(matrix, row_to_modify, row_y, constant):
    for i in range(len(matrix[row_y])):
        matrix[row_to_modify][i] -= matrix[row_y][i] * constant
    print_matrix(matrix)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


def main():
    matrix = [[1, 2, 4, -2], [0, 1, 5, 2], [-2, -4, -3, 9]]
    print_matrix(matrix)
    while True:
        operation = input('Which operation would you like to perform on your matrix? [swap, scale, add, subtract, quit]: ')

        if operation == 'swap':
            row_x = int(input('What is the first row # in the swap? (enter an integer): '))
            row_y = int(input('What is the second row # in the swap? (enter an integer): '))
            swap_rows(matrix, row_x - 1 , row_y - 1)

        elif operation == 'scale':
            scale_factor = input('Would you like to scale by an integer or a fraction? [integer, fraction]:  ')
            if scale_factor == 'integer':
                 row_x = int(input('What is the row # you want to scale? (enter an integer): '))
                 constant = int(input('What is the integer you want to scale this row by?: '))
                 scale_row(matrix, row_x - 1, constant)

            elif scale_factor == 'fraction':
                row_x = int(input('What is the row # you want to scale? (enter an integer): '))
                numerator = int(input('What is the numerator of the fraction you would like to scale this row by?: '))
                denominator = int(input('What is the denominator of the fraction you would like to scale this row by?: '))
                try:
                    constant = Fraction(numerator, denominator)
                except Exception as ex:
                    print(f'Unexpected error occurred when trying to convert your input to a fraction: {ex}')
                scale_row(matrix, row_x - 1, constant)

        elif operation == 'add':
            row_x = int(input('What is the # of the row you would like to add another row to? (enter an integer): '))
            row_y = int(input('What is # of the row that you would like added to the other row? (enter an integer): '))
            constant = int(input('How many times do you want to do this?: '))
            add_row(matrix, row_x - 1, row_y - 1, constant)

        elif operation == 'subtract':
            row_x = int(input('What is the # of the row you would like to subtract another row from? (enter an integer): '))
            row_y = int(input('What is # of the row that you would like subtracted from the other row? (enter an integer): '))
            constant = int(input('How many times do you want to do this?: '))
            subtract_row(matrix, row_x - 1, row_y - 1, constant)

        elif operation == 'quit':
            break

        else:
            print('Invalid operation. Please try again')


if __name__ == "__main__":
    main()
