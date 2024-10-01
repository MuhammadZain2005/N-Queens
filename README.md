# N-Queens Problem Solver

## Description

This project provides a solution to the classic N-Queens problem, a puzzle that involves placing `N` queens on an `N x N` chessboard such that no two queens threaten each other. The solution is implemented in Python and includes a function that prints all possible configurations where the queens are placed safely.

## Features

- **Efficient Backtracking Solution:** Uses a backtracking algorithm to explore all possible placements of queens.
- **Dynamic Board Size:** Works for any value of `N` (e.g., 4, 6, 8), allowing flexible board configurations.
- **Visualization of Solutions:** Prints each solution with `Q` representing a queen and `.` representing empty spaces.

## How It Works

A step-by-step explanation of how the program operates:

1. **Input:** The number of queens (`N`) to be placed on an `N x N` chessboard.
2. **Initialization:** An empty board is initialized, represented as a list of length `N` with all values set to `-1`.
3. **Backtracking Algorithm:** Recursively places queens in each row, ensuring no conflicts in columns and diagonals.
4. **Output:** Prints each valid solution, formatted as a list of strings where `Q` indicates the position of a queen.

## Usage

### Prerequisites

- Python 3.x or any other compatible version.

### Running the Program

1. Clone the repository or download the script file `Daily_Python_22.py`.
2. Run the script using the command:

    ```bash
    python Daily_Python_22.py
    ```

3. Description of expected output:

    ```bash
    Q . . . Q . .
    . . Q . . Q .

    . . . Q Q . .
    ...
    ```

4. Modify the value of `N` in the script to find solutions for different board sizes.

## Program Structure

- **`solve_n_queens(n)`**: The main function that initializes the board and triggers the backtracking solution.
- **`is_safe(board, row, col)`**: Helper function to check whether it is safe to place a queen at a specific position.
- **`solve(board, row, solutions)`**: Recursive function that performs the backtracking.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
