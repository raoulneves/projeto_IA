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
        self.genome = np.full(num_genes, 0, dtype=int)

    def initialize(self):

        # While there are products to be assigned in the list, assign them
        products_to_assign = list(range(len(self.problem.products)))
        agents_to_assign = list(range(len(self.problem.forklifts)))
        index = 0
        agent_separator = 901
        while len(products_to_assign) > 0:
            # Choose where to separate the genome
            #product_placed = random.choice(products_to_assign)
            product_placed = GeneticAlgorithm.rand.choice(products_to_assign)
            self.genome[index] = product_placed

            products_to_assign.remove(product_placed)
            index += 1

        while len(agents_to_assign) > 1:
            if GeneticAlgorithm.rand.random() < 0.8:
                #random_index = random.randrange(len(self.problem.products))
                random_index = GeneticAlgorithm.rand.randrange(len(self.problem.products))
                self.genome = np.insert(self.genome, random_index, agent_separator)
                agent_separator += 1
                agents_to_assign.pop()
            else:
                agents_to_assign.pop()
                self.genome = np.append(self.genome, agent_separator)
                agent_separator += 1
                continue

        self.num_genes = len(self.genome)

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
