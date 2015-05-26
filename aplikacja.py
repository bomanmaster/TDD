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

# Subtracts result of sum_squares from result of square_sum
#
# s1 - result of sum_squares
# s2 - result of square_sum
#   example
#
#   sum_squares = 5, square_sum = 9
#   # => 4
#
# Returns the difference of square_sum result and sum_squares result

    def subtract(self,s1,s2):

        return s2 - s1

def main():

    obj = Sum_of_squares_diffrence()
    s1 = obj.sum_squares()
    s2 = obj.square_sum()

    obj.subtract(s2, s1)

if __name__ == "__main__":
    main()
