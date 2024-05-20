import random

class SnakesAndLadders:
    def __init__(self):
        self.board_size = 100
        self.snakes_and_ladders = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, current_position):
        dice_roll = self.roll_dice()
        new_position = current_position + dice_roll
        if new_position in self.snakes_and_ladders:
            print(f"Player {player} landed on a snake/ladder at position {new_position}!")
            new_position = self.snakes_and_ladders[new_position]
        print(f"Player {player} rolled a {dice_roll}. Current position: {new_position}")
        return new_position

    def check_win(self, player, position):
        if position >= self.board_size:
            print(f"Player {player} wins!")
            return True
        return False

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.game_board = SnakesAndLadders()

    def play_game(self):
        while True:
            for player in self.players:
                input(f"{player.name}, press Enter to roll the dice...")
                player.position = self.game_board.move_player(player.name, player.position)
                if self.game_board.check_win(player.name, player.position):
                    return

if __name__ == "__main__":
    game = Game()
    game.play_game()
