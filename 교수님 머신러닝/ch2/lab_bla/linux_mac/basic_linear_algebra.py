def vector_size_check(*vector_variables):
    return len(zip(vector_variables)) == len(vector_variables[0])


def vector_addition(*vector_variables):
    return [sum(a) for a in zip(vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [a[0] - sum(a) for a in zip(vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * n for n in vector_variable]


def matrix_size_check(*matrix_variables) :    
    return len(zip(matrix_variables)) == len(matrix_variables[0])


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return None
