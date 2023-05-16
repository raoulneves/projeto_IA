
import copy

from agentsearch.problem import Problem
from warehouse.actions import *
from warehouse.cell import Cell
from warehouse.warehouse_state import WarehouseState


class WarehouseProblemSearch(Problem[WarehouseState]):

    def __init__(self, initial_state: WarehouseState, goal_position: Cell):
        super().__init__(initial_state)
        self.actions = [ActionDown(), ActionUp(), ActionRight(), ActionLeft()]
        self.goal_position = goal_position

    def get_actions(self, state: WarehouseState) -> list:
        valid_actions = []
        for action in self.actions:
            if action.is_valid(state):
                valid_actions.append(action)
        return valid_actions

    def get_successor(self, state: WarehouseState, action: Action) -> WarehouseState:
        successor = copy.deepcopy(state)
        action.execute(successor)
        return successor

    def is_goal(self, state: WarehouseState) -> bool:
        # Verifies if the agent is adjacent to the goal position

        if self.goal_position.line == state.line_exit and self.goal_position.column == state.column_exit:
            if state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column:
                return True
            else:
                return False
        else:
            if state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column:
                return True
            elif state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column + 1:
                return True
            elif state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column - 1:
                return True
            elif state.line_forklift == self.goal_position.line + 1 and state.column_forklift == self.goal_position.column:
                return True
            elif state.line_forklift == self.goal_position.line - 1 and state.column_forklift == self.goal_position.column:
                return True
            else:
                return False



    # This method assumes that the tiles in the goal state are ordered from top to bottom, from left to right.
    def compute_path_cost(self, path: list) -> int:
        return len(path)
