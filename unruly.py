from csp import Constraint, NaryCSP, backtracking_search
from csp import mrv, lcv, forward_checking

"""
This program solves the Unruly puzzle as a Constraint Satisfaction Problem (CSP). 
It uses code from the AIMA Python repository: https://github.com/aimacode/aima-python.

Specifically, it uses:
- NaryCSP: Represents the CSP problem.
- Backtracking Search: Solves the problem using:
    - MRV (Minimum Remaining Values) for variable selection,
    - LCV (Least Constraining Value) for value ordering,
    - Forward Checking for maintaining consistency.

The combination of these heuristics ensures efficient and effective exploration of the solution space.
"""


def decode_board(n, m, encoded):
    board = [['' for _ in range(m)] for _ in range(n)]
    x, y = 0, 0
    for char in encoded:
        steps = ord(char.lower()) - ord('a') + 1
        for _ in range(steps):
            if y == m:
                x, y = x + 1, 0
            if x < n and y < m:
                y += 1
        if x < n:
            board[x][y - 1] = 'B' if char.isupper() else 'W'
    return board


def print_board(board):
    for row in board:
        print(' '.join(cell if cell else '.' for cell in row))


def encode_solution(board):
    
    n, m = len(board), len(board[0])
    encoded = []
    steps = 0

    for i in range(n):
        for j in range(m):
            if board[i][j]: 
                letter = chr(ord('a') + steps) 
                if board[i][j] == 'B':  
                    encoded.append(letter.upper())
                else:  
                    encoded.append(letter)
                steps = 0  
            else:
                steps += 1 

    encoded.append('a')

    return f"{n}x{m}:{''.join(encoded)}"


def createCSP(board):
    n = len(board)
    m = len(board[0])

    variables = [(i, j) for i in range(n) for j in range(m)]
    domains = {(i, j): {'B', 'W'} if not board[i][j] else {board[i][j]} for i in range(n) for j in range(m)}

    constraints = []

    for i in range(n):
        for j in range(m - 2):
            scope = [(i, j), (i, j + 1), (i, j + 2)]
            constraints.append(Constraint(scope, lambda a, b, c: not (a == b == c)))

    for i in range(n - 2):
        for j in range(m):
            scope = [(i, j), (i + 1, j), (i + 2, j)]
            constraints.append(Constraint(scope, lambda a, b, c: not (a == b == c)))

    for i in range(n):
        scope = [(i, j) for j in range(m)]
        constraints.append(Constraint(scope, lambda *vals: vals.count('B') == vals.count('W')))

    for j in range(m):
        scope = [(i, j) for i in range(n)]
        constraints.append(Constraint(scope, lambda *vals: vals.count('B') == vals.count('W')))

    return NaryCSP(domains, constraints)


def main():

    print('='*35)
    print('Welcome to the Unruly Solver Pro')
    print('='*35)

    while True:

        filename = input("Give the filename: ")

        if ( filename == 'input.txt'):
            break
        else:
            print('You made a typo error')


    while True:
        try:
            nodes = int(input("Give the max number of nodes: "))
            if nodes > 0:
                break
            else:
                print("The number of nodes must be a positive integer!")
        except ValueError:
            print("Please enter a valid integer for the number of nodes.")


    with open(filename, 'r', encoding='utf-8') as file:
        for data in file:
            dimensions, encode = data.rstrip('\n').split(':')
            n, m = map(int, dimensions.split('x'))

            print(f"Dimensions {n} x {m}")
            print(f"Encoded input {encode}")

            board = decode_board(n, m, encode)
            print("Initial Board:")
            print_board(board)

            csp = createCSP(board)

            print("\nSolving using MRV, LCV and Forward Checking...")
            solution = backtracking_search(
                csp,
                select_unassigned_variable=mrv,
                order_domain_values=lcv,
                inference=forward_checking,
                max_nodes=nodes
            )

            if solution:
                print("\nSolution Found:")
                solved_board = [['' for _ in range(m)] for _ in range(n)]
                for (i, j), value in solution.items():
                    solved_board[i][j] = value
                print_board(solved_board)

                encoded_solution = encode_solution(solved_board)
                print(f"\nEncoded Solution: {encoded_solution}")
            else:
                print("\nNo solution found!")


if __name__ == "__main__":
    main()
