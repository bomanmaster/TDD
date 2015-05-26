__author__ = 'Konrad'

class Sum_of_squares_diffrence:

    def __init__(self):
        pass

    def sum_squares(self):
        suma = 0
        for i in range(1, 11, 1):
            sum = pow(i, 2)
            suma += sum

        return suma