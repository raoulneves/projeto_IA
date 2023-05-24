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

        # Check if the goal position is the same as the exit position
        if self.goal_position.line == state.line_exit and self.goal_position.column == state.column_exit:
            # If the goal position is the same as the exit position, check if the agent (forklift) is currently at the goal position
            if state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column:
                return True
            else:
                return False
        # If the goal position is not the same as the exit position, check if the agent is adjacent to the goal position
        else:
            # # Check if the agent is currently at the goal position
            # if state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column:
            #     return True
            # Check if the agent is to the right of the goal position
            if state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column + 1:
                return True
            # Check if the agent is to the left of the goal position
            elif state.line_forklift == self.goal_position.line and state.column_forklift == self.goal_position.column - 1:
                return True
            else:
                # If the agent is not at the goal position or adjacent to it, return False (the agent is neither at the goal nor adjacent to it)
                return False

    # This method assumes that the tiles in the goal state are ordered from top to bottom, from left to right.
    def compute_path_cost(self, path: list) -> int:
        return len(path)
