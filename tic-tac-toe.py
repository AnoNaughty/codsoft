import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("-" * 9)

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]            # diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return all(val != ' ' for val in self.board)

class AIPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def minimax(self, state, depth, maximizing_player, alpha, beta):
        if state.is_winner(self.symbol):
            return 1
        elif state.is_winner('X' if self.symbol == 'O' else 'O'):
            return -1
        elif state.is_board_full():
            return 0

        if maximizing_player:
            max_eval = -float('inf')
            for move in state.available_moves():
                state.make_move(move, self.symbol)
                eval = self.minimax(state, depth + 1, False, alpha, beta)
                state.make_move(move, ' ')
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in state.available_moves():
                state.make_move(move, 'X' if self.symbol == 'O' else 'O')
                eval = self.minimax(state, depth + 1, True, alpha, beta)
                state.make_move(move, ' ')
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, state):
        best_move = -1
        best_eval = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for move in state.available_moves():
            state.make_move(move, self.symbol)
            eval = self.minimax(state, 0, False, alpha, beta)
            state.make_move(move, ' ')
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

def main():
    game = TicTacToe()
    ai_player = AIPlayer('O')
    human_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    game.display_board()

    while True:
        if game.is_board_full():
            print("It's a draw!")
            break

        human_move = int(input("Enter your move (0-8): "))
        if human_move not in game.available_moves():
            print("Invalid move. Try again.")
            continue

        game.make_move(human_move, human_player)
        game.display_board()

        if game.is_winner(human_player):
            print("You win!")
            break

        if game.is_board_full():
            print("It's a draw!")
            break

        ai_move = ai_player.get_best_move(game)
        game.make_move(ai_move, ai_player.symbol)
        print(f"AI plays move: {ai_move}")
        game.display_board()

        if game.is_winner(ai_player.symbol):
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
