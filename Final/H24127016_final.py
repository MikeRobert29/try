#coding : utf-8

def parse_matrix(matrix_str):
    
    rows = matrix_str.split('|')
    matrix = {}
    for i, row in enumerate(rows):
        elements = row.split(',')
        matrix[i] = [int(element) for element in elements]
    return matrix

def matrix_multiply(U, V, n):
    
    M = {i: [0] * n for i in range(n)}
    for i in range(n):
        for j in range(n):
            M[i][j] = sum(U[i][k] * V[k][j] for k in range(n))
    return M

def matrix_to_string(matrix, n):
    
    rows = []
    for i in range(n):
        row = ','.join(map(str, matrix[i]))
        rows.append(row)
    return '|'.join(rows)

def main():

    U_str = input("Enter matrix U (rows separated by |, elements separated by ,): ")
    V_str = input("Enter matrix V (rows separated by |, elements separated by ,): ")
    

    U = parse_matrix(U_str)
    V = parse_matrix(V_str)
    
    n = len(U)
    
    M = matrix_multiply(U, V, n)
    
    M_str = matrix_to_string(M, n)
    
    print("Resulting matrix M:")
    print(M_str)

if __name__ == "__main__":
    main()