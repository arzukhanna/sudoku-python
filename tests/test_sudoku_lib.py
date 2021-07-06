"""
Unit tests to check functioning of Sudoku solver.
"""

from lib.sudoku import (
    cell_is_valid,
    col_is_valid,
    dimension_is_valid,
    is_grid_valid,
    row_is_valid,
)

GOOD_GRID = [
    [2, 5, 4, 1, 9, 8, 3, 7, 6],
    [8, 1, 7, 4, 3, 6, 5, 2, 9],
    [9, 6, 3, 5, 2, 7, 8, 4, 1],
    [6, 4, 2, 9, 5, 1, 7, 3, 8],
    [5, 8, 1, 2, 7, 3, 9, 6, 4],
    [7, 3, 9, 8, 6, 4, 2, 1, 5],
    [4, 7, 6, 3, 8, 5, 1, 9, 2],
    [1, 9, 8, 7, 4, 2, 6, 5, 3],
    [3, 2, 5, 6, 1, 9, 4, 8, 7]
]

incorrect_dimensions_grid = [
    [2, 5, 4, 1, 9, 8, 3, 7, 6],
    [8, 1, 7, 4, 3, 6, 5, 2, 9],
    [9, 6, 3, 5, 2, 7, 8, 4, 1]
]

row_with_duplicates_grid = [[6, 5, 4, 1, 9, 8, 3, 7, 6]]

column_with_duplicates_grid = [
    [2, 5, 4, 1, 9, 8, 3, 7, 6],
    [8, 1, 7, 4, 3, 6, 5, 2, 9],
    [9, 6, 3, 5, 2, 7, 8, 4, 1],
    [6, 4, 2, 9, 5, 1, 7, 3, 8],
    [5, 8, 1, 2, 7, 3, 9, 6, 4],
    [7, 3, 9, 5, 6, 4, 2, 1, 0],
    [4, 7, 6, 3, 8, 5, 1, 9, 2],
    [2, 9, 8, 7, 4, 0, 6, 5, 3],
    [3, 2, 5, 6, 1, 9, 4, 8, 7]
]

cell_has_letter_grid = [[0, 1, 2, "a", 8, 9, 0, 0, 0, 0]]

cell_outside_range_grid = [[0, 1, 2, 10, 8, 9, 0, 0, 0, 0]]


def test_grid_dimension_is_valid():
    """Test case in which all rows are valid."""
    assert dimension_is_valid(GOOD_GRID)


def test_grid_dimension_is_invalid():
    """Test case in which all rows are valid."""
    assert not dimension_is_valid(incorrect_dimensions_grid)


def test_grid_rows_valid():
    """Test case in which at least one row is invalid."""
    assert row_is_valid(GOOD_GRID)


def test_grid_rows_duplicates_invalid():
    """Test case in which at least one row is invalid."""
    assert not row_is_valid(row_with_duplicates_grid)


def test_column_valid():
    """Test case in which all columns are valid."""
    assert col_is_valid(GOOD_GRID)


def test_grid_cols_duplicates_invalid():
    """Test case in which all columns are valid."""
    assert not col_is_valid(column_with_duplicates_grid)


def test_cell_is_valid():
    """Test case in which all cells are valid."""
    assert cell_is_valid(GOOD_GRID)


def test_cell_has_letter_invalid():
    """Test case in which letter appears in grid."""
    assert not cell_is_valid(cell_has_letter_grid)


def test_cell_outside_range_invalid():
    """Test case in which integer outside correct range appears in grid."""
    assert not cell_is_valid(cell_outside_range_grid)


def test_solved_puzzle_correctly():
    """Test case in which puzzle has been solved correctly."""
    assert is_grid_valid(GOOD_GRID)
