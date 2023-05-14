class Game:
    def __init__(self):
        self.board = [[None for _ in range(19)] for _ in range(19)]
        self.captured = {'black': 0, 'white': 0}

    def place_stone(self, x, y, color):
        self.board[x][y] = color
        captured = self.check_captures(x, y, color)
        self.captured['white' if color == 'black' else 'black'] += captured

    def check_captures(self, x, y, color):
        captured = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and self.board[nx][ny] == ('white' if color == 'black' else 'black'):
                if self.is_captured(nx, ny, []):
                    self.remove_stone(nx, ny)
                    captured += 1
        return captured

    def is_valid(self, x, y):
        return 0 <= x < 19 and 0 <= y < 19

    def is_captured(self, x, y, visited):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and (nx, ny) not in visited:
                if self.board[nx][ny] is None:
                    return False
                elif self.board[nx][ny] == self.board[x][y] and not self.is_captured(nx, ny, visited + [(x, y)]):
                    return False
        return True

    def remove_stone(self, x, y):
        self.board[x][y] = None
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and self.board[nx][ny] is not None:
                self.remove_stone(nx, ny)

    def end_game(self):
        score = {'black': 0, 'white': 0}
        for x in range(19):
            for y in range(19):
                if self.board[x][y] is not None:
                    score[self.board[x][y]] += 1
        score['black'] -= self.captured['black']
        score['white'] -= self.captured['white']
        return score
