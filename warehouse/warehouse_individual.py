import copy

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.steps = 0
        self.path = []

    def compute_fitness(self) -> float:
        # TODO
        self.fitness = 0
        self.steps = 0
        agent = 0
        self.path = [[] for _ in range(len(self.problem.agent_search.forklifts))]
        current_agent = self.path[agent]
        agent_current_position = self.problem.agent_search.forklifts[agent]
        for i, gene in enumerate(self.genome):

            # Check if its 999
            if gene > 900:
                for pair in self.problem.agent_search.pairs:
                    exit = self.problem.agent_search.exit
                    if pair.cell1 == agent_current_position and pair.cell2 == exit:
                        self.fitness += pair.value
                        self.steps += pair.value
                        current_agent.append(pair.solution)
                # Change agent
                agent += 1
                agent_current_position = self.problem.agent_search.forklifts[agent]
                current_agent = self.path[agent]
                continue

            for pair in self.problem.agent_search.pairs:
                product = self.problem.agent_search.products[gene]
                if pair.cell1 == agent_current_position and pair.cell2 == product:
                    self.fitness += pair.value
                    self.steps += pair.value
                    current_agent.append(pair.solution)
                    agent_current_position = product
                    continue

        for pair in self.problem.agent_search.pairs:
            exit = self.problem.agent_search.exit
            if pair.cell1 == agent_current_position and pair.cell2 == exit:
                self.fitness += pair.value
                self.steps += pair.value
                current_agent.append(pair.solution)

        if not self.path:
            print("WHAT THE FUCK?")

        return self.fitness

    def obtain_all_path(self):
        # TODO

        forklift_path = [[] for _ in range(len(self.problem.agent_search.forklifts))]
        # Set starting position for each forklift, should look like this
        # forklift_path = [
        #     [Cell(line=0, column=0)],  # Initial path for forklift 1
        #     [Cell(line=1, column=1)]  # Initial path for forklift 2
        # ]
        for i, forklift in enumerate(self.problem.agent_search.forklifts):
            forklift_path[i].append(Cell(forklift.line, forklift.column))

        number_of_agents = len(self.problem.agent_search.forklifts)

        # Iterate individual path for each forklift
        for i in range(number_of_agents):
            agent_path = self.path[i]
            # Iterate each segment of the total path as a solution
            index = 1
            for solution in agent_path:
                for action in solution.actions:
                    match str(action):
                        case "UP":
                            forklift_path[i].append(Cell(forklift_path[i][index - 1].line - 1, forklift_path[i][index - 1].column))
                            index += 1
                        case "DOWN":
                            forklift_path[i].append(Cell(forklift_path[i][index - 1].line + 1, forklift_path[i][index - 1].column))
                            index += 1
                        case "LEFT":
                            forklift_path[i].append(Cell(forklift_path[i][index - 1].line ,forklift_path[i][index - 1].column - 1))
                            index += 1
                        case "RIGHT":
                            forklift_path[i].append(Cell(forklift_path[i][index - 1].line ,forklift_path[i][index - 1].column + 1))
                            index += 1
                        case _:  # Default case
                            print("Invalid action")


        return forklift_path, self.steps

    def __str__(self):
        string = 'Fitness: ' + str(self.fitness) + '\n'
        string += "Genome: " + str(self.genome) + "\n"

        data = self.genome.tolist()  # Convert the genome to a Python list

        # Get the maximum agent ID
        max_agent_id = 1
        for data_point in data:
            if data_point > 900:
                max_agent_id += 1

        # Initialize the columns
        columns = [[] for _ in range(max_agent_id)]

        # Populate the columns with product IDs in the order of appearance
        agent_id = 0
        for data_point in data:
            if data_point > 900:
                agent_id += 1
                continue
            columns[agent_id].append(data_point)

        # Determine the maximum number of products in a column
        max_products = max(len(column) for column in columns)

        # Determine the maximum number of digits in product IDs
        max_digits_number = 0
        for column in columns:
            if column:
                max_digits_number = max(max_digits_number, len(str(max(column))))

        # Determine the maximum number of digits in the word Agent X
        max_digits_word = len("Agent " + str(max_agent_id))

        # Check which is bigger
        max_digits = max(max_digits_number, max_digits_word)

        # Build the table string
        table = ""
        for i in range(max_products):
            table += "|"
            for column in columns:
                if i < len(column):
                    table += f" {column[i]:{max_digits-1}} |"
                else:
                    table += " " * (max_digits + 1) + "|"
            table += "\n"

        # Add the header row
        header = "|"
        for i in range(1, max_agent_id + 1):
            header += f"Agent {i} |"
        table = f"+{'-' * ((max_digits + 2) * max_agent_id - 1)}+\n" + header + "\n" + table
        table += f"+{'-' * ((max_digits + 2) * max_agent_id - 1)}+\n"

        return string + table

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.path = self.path
        new_instance.steps = self.steps
        # TODO
        return new_instance
