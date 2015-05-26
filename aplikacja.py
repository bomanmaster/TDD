__author__ = 'Konrad'

class Sum_of_squares_diffrence:

    def __init__(self):
        pass

# Squares first 10 natural numbers and adds them
#
# sum - sum of squared numbers
# pow_sum - sum of individual squared number
#
#   example
#
#   sum of squares of 2 natural numbers (1,2)
#   # => 5
#
# Returns the sum of the squared numbers(first 10 natural numbers)

    def sum_squares(self):

        sum = 0

        for i in range(1, 11, 1):
            pow_sum = pow(i, 2)
            sum += pow_sum

        return sum


# Adds first 10 natural numbers and then squares the sum
#
# sum - sum of first 10 natural numbers
#
#   example
#
#   squared sum of 2 first natural numbers(1,2)
#   # => 9
#
# Returns the result of squared sum of first 10 natural numbers

    def square_sum(self):

        sum = 0
        for i in range(1,11,1):
            sum += i

        return pow(sum,2)
