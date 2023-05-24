from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

        # Not s ure yet
        self.pairs = agent_search.pairs
        self.exit = agent_search.exit

        # Generate a list of tuples with the index and the forklift
        tuple_agent_list = [(i, forklift) for i, forklift in enumerate(self.agent_search.forklifts)]
        self.agents_db = tuple(tuple_agent_list)

        # Generate a list of tuples with the index and the product
        tuple_product_list = [(i, product) for i, product in enumerate(self.agent_search.products)]
        self.products_db = tuple(tuple_product_list)

    def generate_individual(self) -> "WarehouseIndividual":
        # Genome length is the number of products
        new_individual = WarehouseIndividual(self, len(self.products))
        new_individual.initialize()
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string
