from pyperclip import copy
import utils


class Board:
    def __init__(self, array):
        self.board = [list(map(int, line.split())) for line in array]
        self.pending = set()
        for lst in self.board:
            self.pending.update(lst)
        self.marked = [[0 for _ in range(5)] for _ in range(5)]

    def put(self, number):
        if number in self.pending:
            self.pending.remove(number)
            for i in range(5):
                for j in range(5):
                    if self.board[i][j] == number:
                        self.marked[i][j] = 1
                        if self.check_won(i, j):
                            return self.value(number)

        return 0

    def check_won(self, i, j):
        if all(self.marked[i]):
            return True
        if all(self.marked[i2][j] for i2 in range(5)):
            return True
        return False

    def value(self, number):
        suma = 0
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    suma += self.board[i][j]
        return suma * number


def get_lines():
    return utils.get_input(4)


def create_boards(lines):
    numbers = list(map(int, lines[0].split(',')))
    boards = []
    i = 2
    while i < len(lines):
        boards.append(Board(lines[i:i + 5]))
        i += 6
    return boards, numbers


def part1(lines):
    boards, numbers = create_boards(lines)
    for numb in numbers:
        for board in boards:
            won = board.put(numb)
            if won:
                return won


def part2(lines):
    boards, numbers = create_boards(lines)

    boards = boards[::-1]  # WTF els últims 2 guanyen al mateix temps????, i només 1 és la resposta correcta...

    for numb in numbers:
        new_boards = []
        for board in boards:
            won = board.put(numb)
            if not won:
                new_boards.append(board)
        boards = new_boards
    return won


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
