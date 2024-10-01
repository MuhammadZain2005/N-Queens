"""
N-Queens problem
"""
def solve_n_queens(n):
    # Helper function to check if placing a queen at board[row] = col is safe
    def is_safe(board, row, col):
        # Check if the column had a queen before.
        for i in range(row):
            # Check if a queen is in the same column
            if (board[i] == col or \
                    # Check if a queen is in the same diagonal (left or right)
                    board[i] - i == col - row or \
                    board[i] + i == col + row):
                return False
        # If no conflict, queen is safe in that box
        return True

    # Recursive Function to place queens
    def solve(board, row, solutions):
        # Base Case
        if row == n:
            # Convert the board representation to the expected format
            solution = []
            for i in range(n):
                # Create a string with . for empty spaces and Q for queens
                row_str = '.' * board[i] + 'Q' + '.' * (n - board[i] - 1)
                solution.append(row_str)
            # Add this solution to list of solutions
            solutions.append(solution)
            return
        # Try placing queen in each column
        for col in range(n):
            # Check if it's safe to place queen, then recursively put in next row
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1, solutions)
                # Backtrack (not needed here since we overwrite board[row] on the next loop)

    solutions = []
    board = [-1] * n
    solve(board, 0, solutions)

    # Print each solution on a new line
    for solution in solutions:
        for row in solution:
            print(row)
        print()  # Add a blank line between solutions

    return solutions

# Example usage:
solve_n_queens(6)
