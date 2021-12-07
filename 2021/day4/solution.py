import numpy as np



class SubBingo:
    def __init__(self, filename):
        numbers = []
        boards = []
        with open(filename) as f:
            self.numbers = np.array(f.readline().strip().split(",")).astype(int)
            for line in f:
                if line.strip() == "":
                    boards.append([])
                    continue
                boards[-1].append(np.array(line.strip().split()).astype(int))
        self.boards = np.array(boards)

    def set_selected_number(self, number):
        self.boards[self.boards == number] = -1

    def get_winning_board(self, sums):
        print(sums)
        indices = np.where(sums == -5)
        print(indices)
        breakpoint()
        board_index = indices[0][0]
        return self.boards[board_index], board_index

    def check_for_winning_board(self):
        col_sums = self.boards.sum(axis=1)
        row_sums = self.boards.sum(axis=2)
        board = None
        board_index = None
        if -5 in col_sums:
            board, board_index = self.get_winning_board(col_sums)
        elif -5 in row_sums:
            board, board_index = self.get_winning_board(row_sums)
        return board, board_index

    def get_board_score(self, board, number):
        unmarked_sum = board[board != -1].sum()
        return unmarked_sum * number

    def play(self):
        for i, number in enumerate(self.numbers):
            if self.iter(number, i):
                break


class WinSubBingo(SubBingo):
    def iter(self, number, i=None):
        self.set_selected_number(number)
        board, _ = self.check_for_winning_board()
        if board is not None:
            score = self.get_board_score(board, number)
            print(f"The first board won: {board}. Score: {score}")
            return True


class LoseSubBingo(SubBingo):
    def __init__(self, filename):
        super(LoseSubBingo, self).__init__(filename)
        self.num_boards = self.boards.shape[0]
        self.boards_won = 0

    def iter(self, number, i):
        self.set_selected_number(number)
        board, board_index = self.check_for_winning_board()
        if board is not None:
            self.boards_won += 1
            if self.boards_won == self.num_boards or i == len(self.numbers) - 1:
                score = self.get_board_score(board, number)
                print(f"The last board won: {board}. Score: {score}")
                return True
            indices = [index for index in range(self.boards.shape[0]) if index != board_index]
            self.boards = self.boards[indices]



print("Part 1")
win = WinSubBingo("input.txt")
win.play()


print("Part 2")
lose = LoseSubBingo("input.txt")
lose.play()
