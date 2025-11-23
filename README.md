# Project 05
**CS-1160 Wright State University | Dan Grahn**

> Reminder: In order to maintain academic integrity, you are required to cite any assistance you received outside of course materials. See [Citing Sources](citing.md) for examples.

## Introduction
Battleship is a classic board game which originated in the 1930s. The rules for Battleship can be found [here](https://www.hasbro.com/common/instruct/Battleship.PDF).

In this project you will implement two classes to support a Battleship game. The first class, a "Grid", maintains the state of a single player's ocean grid (see the rules). The second class, a "Player" will be an autonomous player.

Your Grid implementation will be evaluated for correctness. However, your player implementation will be evaluated against 5 other autonomous players.

1. Simple Player -Always places its ships in the same locations. It targets from the top-left to the bottom-right in order. The implementation is available under `players.py`.
2. Random Player - Randomly places ships and randomly targets locations.
3. Basic Player - Randomly places ships, but targets using a basic algorithm.
4. Advanced Player - Randomly places ships and targets using an advanced algorithm.
5. Super Player - Optimized ship placement and an extra advanced targeting algorithm.

Additionally, we will have a competition where each players compete against each other. There will be rewards for the top-3 contestants. For information on how to compare players, see `score.py`.

`game.py` will work once a valid grid object is stored.

## Details

### Grid
Your implementation of the ocean grid must use `Grid` as a base class and implement five methods. Put the code for your grid in `my_grid.py`.

#### `get(position) -> Cell`
This method returns an instance of `Cell` which contains the details of the cell in the grid. `Cell` contains information on whether the cell has been targeted and any ship it contains. There are 100 cells in the grid named A1-J10.

#### `is_valid(position, orientation, ship) -> bool`
This method checks whether a specific placement of a ship is valid. If the orientation is "horizontal", the position indicates the furthest left location of the ship. If the orientation is "vertical" the position indicates the furthest up location of the ship.

#### `place(position, orientation, ship) -> bool`
This method places a ship on the grid. It returns `True` if the ship was able to be placed at the requested location and `False` otherwise.

#### `target(position) -> MoveResult`
This method calculates the effects of targeting a specific position. It returns a `MoveResult` which indicates whether the result was a hit, the hit ship, and if it was sunk.

#### `all_sunk() -> bool`
This method checks if all the ships are sunk.


### Player
Your Player implementation must use `Player` as a base class and implement two methods.  Name your player implementation `[First Initial][Last Name]Player`.  Put the code for your play in `my_player.py`.

#### `place_ships(grid)`
This method places the ships on the grid that is given as an argument.

### `get_move() -> str`
This method returns a move for to make.

### `log_result(result)`
This method is optional. You do not need to implement it, but it is how the game will report the results of your move.


## Grading
Grading will not be done automatically on push like the labs. Instead, it will be performed after final submission. Your application will be tested against a range of inputs which are designed to make it fail. It will be graded against the following criteria.

1. Grid Implementation
    * `get` method (15 pts implementation, 5 pts documentation)
    * `is_valid` method (15 pts implementation, 5 pts documentation)
    * `place` method (15 pts implementation, 5 pts documentation)
    * `target` method (15 pts implementation, 5 pts documentation)
    * `all_sunk` method (15 pts implementation, 5 pts documentation)

2. Player Implementation
    * Random Player - Full points for beating it > 50% of the time (10 pts)
    * Simple Player - Full points for beating it > 50% of the time (15 pts)
    * Basic Player - Partial points for win %. (30 pts)
    * Advanced Player - Partial points for win %.  (20 pts)
    * Super Player - Partial points for wins %. (+ 50 bonus pts)

Take time to consider the different "edge cases" that could be given to your application. 