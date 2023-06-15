from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self, problem: WarehouseProblemSearch):
        super().__init__()
        self.problem = problem

    def compute(self, state: WarehouseState) -> float:
        # TODO
        # The heuristic value is the Manhattan distance between the forklift and the GOAL POSITION
        forklift_pos = (state.line_forklift, state.column_forklift)
        goal_pos = (self.problem.goal_position.line, self.problem.goal_position.column)

        heuristic_value = abs(forklift_pos[0] - goal_pos[0]) + abs(forklift_pos[1] - goal_pos[1])

        return heuristic_value

    def __str__(self):
        return "# TODO"

