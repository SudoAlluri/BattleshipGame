from grid import Grid
from players import Player
from ships import Ships
from helpers import MoveResult, Orientation
import random
from my_grid import my_grid 

class FirstInitialLastNamePlayer(Player):
    """An battleship player."""
    def __init__(self) -> None:
        self.grid_cells = []
        self.orientations = ['h','v']
        self.diag1 = []
        self.diag2 = []
        self.attacked_ships = []
        self.mode = 'F'
        self.ship_to_sink = None
        #grid boxes
        for row in range(10):
            for col in range(10):
                #box Name
                cell_name = my_grid.xy_to_pos(row,col)
                self.grid_cells.append(cell_name)
        
        #diagonal boxes
        for row in range(10):
            for col in range(10):
                if (row + col) % 2 == 1:
                    self.diag1.append(my_grid.xy_to_pos(row,col))
                else:
                    self.diag2.append(my_grid.xy_to_pos(row,col))


    def log_result(self, result:MoveResult) -> None:
        
        self.attacked_ships.append(result)
        if result.ship:
            if result.is_sunk: # After sinking the ship, setting the mode to F
                self.mode = 'F' #Find
            else: #Sink the ship on one hit and set the mode to S
                self.mode = 'S' # Sink
                self.ship_to_sink = result.ship            
        pass

    def place_ships(self, grid:my_grid) -> None:
        #Place Ships Dynamicallys
        #1.Select a cell from the grid
        #2.Check the cell is valid Use my_grid.is_valid() Hint # Pick the random orientation
        #3.If it is valid, then check the surrounding cells Hint: Increase x and y coordinates by 1 and check the positions have ships
        #4.If there are no nearby ships, place your ship
        grid.place('B3', Orientation.HORIZONTAL, Ships.CARRIER)
        grid.place('D9', Orientation.VERTICAL, Ships.BATTLESHIP)
        grid.place('E6', Orientation.VERTICAL, Ships.CRUISER)
        grid.place('I2', Orientation.HORIZONTAL, Ships.SUBMARINE)
        grid.place('E2', Orientation.HORIZONTAL, Ships.DESTROYER)

        

    def get_move(self) -> str:
        move = 0
        if self.mode == 'F':
            if len(self.diag1) > 0:
                move = random.choice(self.diag1)
                self.diag1.remove(move)
                self.grid_cells.remove(move)
            elif len(self.diag2) > 0:
                move = random.choice(self.diag2)
                self.diag2.remove(move)
                self.grid_cells.remove(move)
            elif len(self.grid_cells) > 0:
                move = random.choice(self.grid_cells)
                self.grid_cells.remove(move)
            return move
        