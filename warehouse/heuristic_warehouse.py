from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # TODO
        # The heuristic value is the Manhattan distance between the forklift and the exit
        forklift_pos = (state.line_forklift, state.column_forklift)
        exit_pos = (state.line_exit, state.column_exit)

        heuristic_value = abs(forklift_pos[0] - exit_pos[0]) + abs(forklift_pos[1] - exit_pos[1])

        return heuristic_value

    def __str__(self):
        return "HeuristicWarehouse"
