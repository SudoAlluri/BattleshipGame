from my_grid import my_grid
from players import SimplePlayer, RandomPlayer
from battleship import Battleship
from grid import Grid

NUM_TESTS = 1_000

winners = { 1: 0, 2: 0 }
moves = { 1: [], 2: [] }

for i in range(NUM_TESTS):
    if i % 100 == 0: print(i)

    player_one = SimplePlayer()
    player_two = RandomPlayer()

    grid_one = my_grid() # Replace with an instance of your grid
    grid_two = my_grid() # Replace with an instance of your grid

    game = Battleship(
        player_one, player_two,
        grid_one, grid_two,
        debug=False
    )

    game.setup()
    winner, num_moves = game.play()
    winners[winner] += 1
    moves[winner].append(num_moves)


print(f'Player 1 won {winners[1]:,d} games with {sum(moves[1]) / len(moves[1]):.2f} average # moves.')
print(f'Player 2 won {winners[2]:,d} games with {sum(moves[2]) / len(moves[2]):.2f} average # moves.')