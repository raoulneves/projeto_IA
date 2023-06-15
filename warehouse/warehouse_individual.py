from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.steps = 0

    def compute_fitness(self) -> float:
        # TODO

        self.steps = 0

        for i, gene in enumerate(self.genome):
            if i == 0:
                product_tofetch = self.problem.product[gene]
                agent_fetching = self.problem.agent[gene + 1]
            else:
                product_tofetch = self.problem.product[gene + 1]
                agent_fetching = self.problem.agent[gene + 2]

            agent_location = self.problem.agent[agent_fetching]
            product_location = self.problem.product[product_tofetch]

            for pairs in self.problem.pairs:
                if pairs.cell1 == agent_location and pairs.cell2 == product_location:
                    self.steps += pairs.value
                elif pairs.cell1 == product_location and pairs.cell2 == agent_location:
                    self.steps += pairs.value
                else:
                    print("ERROR NO PAIR! AGENT: ", agent_location, " PRODUCT: ", product_location)

        return self.steps

    def obtain_all_path(self):
        # TODO
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # TODO
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
