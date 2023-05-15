from typing import TypeVar  # Used for type hinting

import numpy as np  # Used for numerical computations

# Importing different modules and classes
import constants
from agentsearch.agent import Agent
from agentsearch.state import State
from warehouse.cell import Cell
from warehouse.heuristic_warehouse import HeuristicWarehouse
from warehouse.pair import Pair


class WarehouseAgentSearch(Agent):
    S = TypeVar('S', bound=State)  # A type variable bound to the State class

    def __init__(self, environment: S):  # Initializing the WarehouseAgentSearch class
        super().__init__()  # Calling the init method of the parent class
        self.initial_environment = environment  # Storing the initial environment
        self.heuristic = HeuristicWarehouse()  # Setting up the heuristic
        self.forklifts = []  # List for storing forklift locations
        self.products = []  # List for storing product locations
        self.exit = None  # Variable for storing the exit location
        self.pairs = []  # List for storing pairs of locations
        # Looping over the environment matrix to find forklifts, exits and products
        for i in range(environment.rows):
            for j in range(environment.columns):
                if environment.matrix[i][j] == constants.FORKLIFT:
                    self.forklifts.append(Cell(i, j))
                elif environment.matrix[i][j] == constants.EXIT:
                    self.exit = Cell(i, j)
                elif environment.matrix[i][j] == constants.PRODUCT:
                    self.products.append(Cell(i, j))

        # Creating pairs of forklifts and products
        for a in self.forklifts:
            for p in self.products:
                self.pairs.append(Pair(a, p))

        # Creating pairs of products
        for i in range(len(self.products) - 1):
            for j in range(i + 1, len(self.products)):
                self.pairs.append(Pair(self.products[i], self.products[j]))

        # Creating pairs of products and exit
        for p in self.products:
            self.pairs.append(Pair(p, self.exit))

        # Creating pairs of forklifts and exit
        for a in self.forklifts:
            self.pairs.append(Pair(a, self.exit))

    def __str__(self) -> str:  # String representation of WarehouseAgentSearch
        str = "Pairs:\n"
        for p in self.pairs:
            str += f"{p}\n"
        return str


def read_state_from_txt_file(filename: str):  # Function to read state from a text file
    with open(filename, 'r') as file:
        num_rows, num_columns = map(int, file.readline().split())
        float_puzzle = np.genfromtxt(file, delimiter=' ')
        return float_puzzle, num_rows, num_columns
