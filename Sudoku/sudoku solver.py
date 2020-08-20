import sys
def get_possible_numbers(y, x):
    numbers = list(range(1, 10))
    for i in range(9):
        k = board[y][i]
        if k != 0 and k in numbers:
            numbers.remove(k)
    if not numbers:
        return []
    for i in range(9):
        k = board[i][x]
        if k != 0 and k in numbers:
            numbers.remove(k)
    if not numbers:
        return []
    curr_x = (x // 3) * 3
    curr_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            k = board[curr_y + i][curr_x + j]
            if k != 0 and k in numbers:
                numbers.remove(k)
    return numbers


def validate(y, x, n):
    # Row Check
    for i in range(9):
        if board[y][i] == n:
            return False
    # Column Check
    for i in range(9):
        if board[i][x] == n:
            return False
    curr_x = (x // 3) * 3
    curr_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[curr_y + i][curr_x + j] == n:
                return False
    return True

def solve(z_at = 0):
    zx, zy = zeroes[z_at][1], zeroes[z_at][0]
    for n in get_possible_numbers(zy, zx):
        if validate(zy, zx, n):
            board[zy][zx] = n
            if z_at + 1 == len(zeroes):
                for i in range(9):
                    for j in range(9):
                        print(board[i][j], end=" ")
                    print()
                sys.exit(0)
            solve(z_at+1)
            board[zy][zx] = 0

board, zeroes = {}, []
zero_candidates = []
if __name__ == "__main__":
    input = sys.stdin.readline
    for i in range(9):
        row = list(map(int, input().split()))
        for j in range(9):
            if row[j] == 0:
                zeroes.append((i, j))
        board[i] = row
    # for zero in zeroes:
    #     numbers = get_possible_numbers(*zero)
    #     zero_candidates.append(numbers)
    solve()