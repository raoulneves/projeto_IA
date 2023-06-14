import copy
from typing import TypeVar

import numpy as np

import constants
from agentsearch.agent import Agent
from agentsearch.state import State
from warehouse.cell import Cell
from warehouse.heuristic_warehouse import HeuristicWarehouse
from warehouse.pair import Pair


class WarehouseAgentSearch(Agent):
    S = TypeVar('S', bound=State)

    def __init__(self, environment: S):
        super().__init__()
        self.initial_environment = environment
        self.heuristic = HeuristicWarehouse()
        self.forklifts = []
        self.products = []
        self.exit = None
        self.pairs = []
        for i in range(environment.rows):
            for j in range(environment.columns):
                if environment.matrix[i][j] == constants.FORKLIFT:
                    self.forklifts.append(Cell(i, j))
                elif environment.matrix[i][j] == constants.EXIT:
                    self.exit = Cell(i, j)
                elif environment.matrix[i][j] == constants.PRODUCT:
                    self.products.append(Cell(i, j))

        # Change the position of the products so that path finding is easier
        fixed_products_pickup = copy.deepcopy(self.products)
        for i in range(len(fixed_products_pickup)):
            # Empty on the left
            if constants.EMPTY == \
                    environment.matrix[fixed_products_pickup[i].line][fixed_products_pickup[i].column - 1]:
                fixed_products_pickup[i].column -= 1
            # Empty on the right
            elif constants.EMPTY == \
                    environment.matrix[fixed_products_pickup[i].line][fixed_products_pickup[i].column + 1]:
                fixed_products_pickup[i].column += 1

        # Forklifts - Products
        for a in self.forklifts:
            for p in fixed_products_pickup:
                self.pairs.append(Pair(a, p))

        # Products - Products
        for i in range(len(fixed_products_pickup) - 1):
            for j in range(i + 1, len(fixed_products_pickup)):
                self.pairs.append(Pair(fixed_products_pickup[i], fixed_products_pickup[j]))

        # Products - Exit
        for p in fixed_products_pickup:
            self.pairs.append(Pair(p, self.exit))

        # Forklifts - Exit
        for a in self.forklifts:
            self.pairs.append(Pair(a, self.exit))

    def __str__(self) -> str:
        str = "Pairs:\n"
        for p in self.pairs:
            str += f"{p}\n"
        return str


def read_state_from_txt_file(filename: str):
    with open(filename, 'r') as file:
        num_rows, num_columns = map(int, file.readline().split())
        float_puzzle = np.genfromtxt(file, delimiter=' ')
        return float_puzzle, num_rows, num_columns
