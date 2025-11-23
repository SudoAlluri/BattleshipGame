
# FIXME Put your grid in this file.
from turtle import pos
from grid import Grid
from helpers import MoveResult, Orientation, Cell
from ships import Ship, Ships
from typing import Tuple

class my_grid(Grid):
    def __init__(self) -> None:
        #build empty grid of 10 x 10
        self.ships = {}
        self.grid = {}
        self.placed_ships = {}
        for i in Ships.ALL:
            self.ships[i.name] = 0
        for row in range(10):
            for col in range(10):
                cell_name = self.xy_to_pos(row,col) #Cell Name
                self.grid[cell_name] = Cell(False,None)
                

    def get(self, position:str) -> Cell:
        return self.grid[position]

    def is_valid(self, position:str, orientation:Orientation, ship:Ship) -> bool:

        ship_size = ship.size
        cell = self.grid[position]
        if cell.ship:
            return False #Position is already occupied by a ship
        else:
            if orientation == Orientation.HORIZONTAL:
                # print('H')
                #logic to get next ship size cells Horizontally
                # logic for horizontal check
                x,y = self.pos_to_xy(position)
                if y + ship_size > 10:
                    return False
                else:
                    # return True
                    for i in range(ship_size-1):
                        pos = self.xy_to_pos(x,y+i)
                        cell = self.grid[pos]
                        if cell.ship:
                            return False
            elif orientation == Orientation.VERTICAL:
                # print('V')
                x,y = self.pos_to_xy(position)
                if x + ship_size > 10:
                    return False
                else:
                    for i in range(ship_size-1):
                        pos = self.xy_to_pos(x+i,y)
                        cell = self.grid[pos]
                        if cell.ship:
                            return False
        return True
     
    def place(self, position:str, orientation:Orientation, ship:Ship) -> bool:
        ship_size = ship.size
        cell = self.grid[position]
        if self.is_valid(position,orientation,ship) == True:
            x,y = self.pos_to_xy(position)
            if orientation == Orientation.HORIZONTAL:
                for i in range(ship_size-1):
                        pos = self.xy_to_pos(x,y+i)
                        cell = self.grid[pos]
                        cell.ship = ship
                        self.grid[pos] = cell
            elif orientation == Orientation.VERTICAL:
                for i in range(ship_size-1):
                        pos = self.xy_to_pos(x+i,y)
                        cell = self.grid[pos]
                        cell.ship = ship
                        self.grid[pos] = cell
            self.placed_ships[ship.name] = ship_size
            return True
        else:
            return False

    def target(self, position:str) -> MoveResult:
        try:
            cell = self.grid[position]
            cell.targeted = True
            self.grid[position] = cell
            if cell.ship:
                num_hits = self.ships[cell.ship.name]
                num_hits += 1
                if num_hits >= cell.ship.size:
                    is_sunk = True
                else:
                    is_sunk = False
                self.ships[cell.ship.name] = num_hits
            else:
                is_sunk = False
            return MoveResult(position,cell.ship,is_sunk)
        except:
            print('Exception occurred')
            return MoveResult(position,None,False)

    def all_sunk(self) -> bool:
        num_ships = len(self.ships)
        num_ships_sunk = 0
        for i in self.ships.keys():
            num_hits = self.ships[i]
            ship_size = self.placed_ships[i]
            if num_hits >= ship_size:
                num_ships_sunk += 1
        if num_ships_sunk == num_ships:
            return True
        else:
            return False

    def __str__(self):
        r  = '    1 2 3 4 5 6 7 8 9 10\n'
        r += '  ╔═════════════════════╗\n'

        for x in range(10):
            r += f'{chr(x + 65)} ║ '

            for y in range(10):
                pos = Grid.xy_to_pos(x, y)
                cell = self.get(pos)
                r += f'{cell} '
            r += '║\n'
        r += '  ╚═════════════════════╝'
        return r

# G = my_grid()
# # print(G.grid)
# print(G.grid['A1'])
