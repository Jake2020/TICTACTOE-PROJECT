from project import print_board, get_move, check_win

def test_print_board(capsys):
    # Use pytests output capture functionality to capture output of print_board()
    board = [['X', 'O', '-'], ['-', 'X', '-'], ['O', '-', 'O']]
    print_board(board)
    captured = capsys.readouterr()
    assert captured.out == '| X | O | - |\n| - | X | - |\n| O | - | O |\n'

    board2 = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print_board(board2)
    captured2 = capsys.readouterr()
    assert captured2.out == '| - | - | - |\n| - | - | - |\n| - | - | - |\n'


def test_check_win():
    # Check boards result in correct winner
    board1 = [['X', 'O', '-'], ['-', 'X', '-'], ['O', '-', 'O']]
    assert check_win(board1, 'X') == False
    assert check_win(board1, 'O') == False

    board2 = [['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]
    assert check_win(board2, 'X') == True
    assert check_win(board2, 'O') == False

    board3 = [['X', '-', 'O'], ['-', 'X', 'O'], ['-', '-', 'O']]
    assert check_win(board3, 'O') == True
    assert check_win(board3, 'X') == False


def test_get_move(monkeypatch):
    # Use pytests input feature to check correct values assigned
    monkeypatch.setattr('builtins.input', lambda _: '1 2')
    row, col = get_move('X')
    assert row == 1
    assert col == 2

    monkeypatch.setattr('builtins.input', lambda _: '0 0')
    row, col = get_move('X')
    assert row == 0
    assert col == 0