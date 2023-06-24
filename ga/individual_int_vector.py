import random
from abc import abstractmethod

import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        # self.genome = np.full((num_genes, 2), 0, dtype=int)
        self.genome = [[0, 0] for _ in range(num_genes)]

    def initialize(self):
        # While there are products to be assigned in the list, assign them
        products_to_assign = list(range(len(self.problem.products)))
        agents_to_assign = list(range(len(self.problem.forklifts)))
        GeneticAlgorithm.rand.shuffle(products_to_assign)
        # Generate the genome by randomly assigning products to agents
        # genome = [(product, random.choice(agents)) for product in products]
        for i, product_id in enumerate(products_to_assign):
            agent_id = GeneticAlgorithm.rand.choice(agents_to_assign)

            self.genome[i] = [product_id, agent_id]
            # self.genome[i][0] = product_id
            # self.genome[i][1] = agent_id

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
