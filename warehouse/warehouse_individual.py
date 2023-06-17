from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.steps = 0

    def compute_fitness(self) -> float:
        # TODO

        self.steps = 0
        agent = 0
        agent_current_position = self.problem.agent_search.forklifts[agent]

        for i, gene in enumerate(self.genome):

            # Check if its 999
            if gene == 999:
                # AND if it is not the last gene
                if i+1 < len(self.genome):
                    if self.genome[i + 1] != 999 and self.genome[i + 1] is not None:
                        agent += 1
                        agent_current_position = self.problem.agent_search.forklifts[agent]
                        continue
                    else:
                        continue
                else:
                    continue

            for pairs in self.problem.agent_search.pairs:
                if pairs.cell1 == agent_current_position and pairs.cell2 == self.problem.agent_search.products[gene]:
                    self.steps += pairs.value
                    agent_current_position = self.problem.agent_search.products[gene]
                elif pairs.cell1 == self.problem.agent_search.products[gene] and pairs.cell2 == agent_current_position:
                    self.steps += pairs.value
                    agent_current_position = self.problem.agent_search.products[gene]

        for pairs in self.problem.agent_search.pairs:
            if pairs.cell1 == agent_current_position and pairs.cell2 == self.problem.agent_search.exit:
                self.steps += pairs.value
            elif pairs.cell2 == self.problem.agent_search.exit and pairs.cell2 == agent_current_position:
                self.steps += pairs.value

        self.fitness = self.steps

        return self.steps

    def obtain_all_path(self):
        # TODO
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += "Genome: " + str(self.genome) + "\n"
        # TODO
        agent = 0
        for i, gene in enumerate(self.genome):
            # Agent updater
            if gene == 999:
                # AND if it is not the last gene
                if i + 1 < len(self.genome):
                    if self.genome[i + 1] != 999 and self.genome[i + 1] is not None:
                        agent += 1
                        continue
                    else:
                        continue
                else:
                    continue
            string += "Agent " + f"{agent+1}:\t" + str(gene+1) + "\n"

        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance
