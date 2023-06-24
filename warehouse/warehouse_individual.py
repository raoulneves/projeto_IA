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
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += "Genome: " + str(self.genome) + "\n"
        # TODO
        agent = 0
        for i, gene in enumerate(self.genome):
            # Agent updater
            if gene > 900:
                # AND if it is not the last gene
                if i + 1 < len(self.genome):
                    if self.genome[i + 1] < 900 and self.genome[i + 1] is not None:
                        agent += 1
                        continue
                    else:
                        continue
                else:
                    continue
            string += "Agent " + f"{agent + 1}:\t" + str(gene + 1) + "\n"

        return string

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
