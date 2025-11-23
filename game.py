from my_grid import my_grid
from my_player import FirstInitialLastNamePlayer
from players import RandomPlayer
from battleship import Battleship
from grid import Grid

#player_one = SimplePlayer()
player_one = FirstInitialLastNamePlayer()
player_two = RandomPlayer()

grid_one = my_grid() 
grid_two = my_grid() 
game = Battleship(
    player_one, player_two,
    grid_one, grid_two,
    debug=True
)

game.setup()
winner, moves = game.play()
print(f'Player {winner} won in {moves} moves.')