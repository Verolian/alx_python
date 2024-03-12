def square_matrix_simple(matrix):
    # Create a new matrix to store squared values
    result_matrix = []
    
    # Iterate through the rows in the input matrix
    for row in matrix:
        squared_row = []  # Create a new row for the result matrix
        for element in row:
            squared_row.append(element ** 2)  # Compute the square of each element and append to the new row
        result_matrix.append(squared_row)  # Append the new row to the result matrix
    
    return result_matrix  # Return the new matrix containing squared values