from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.steps = None
        self.picked_products = None

    def compute_fitness(self) -> float:
        # TODO

        self.steps = 0
        self.picked_products = 0

        for i, agent in enumerate(self.agents):
            agent_id = agent[0]
            agent_pos = agent[1]
            for j, product in enumerate(self.genome):
                product = self.genome[j, 0]
                agent_genome = self.genome[j, 1]

                if agent_id == agent_genome:
                    # self.steps += self.
                    self.picked_products += 1

        return 0

    def obtain_all_path(self):
        # TODO
        # Final step after running GA
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
