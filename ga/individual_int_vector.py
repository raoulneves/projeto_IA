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

    def initialize(self, prob1s: float):
        # Create pool of product numbers
        # Generate the genome by randomly assigning products to agents
        # genome = [(product, random.choice(agents)) for product in products]
        for i, product in enumerate(self.problem.products * self.problem.agents):
            agent_id = random.choice(self.problem.agents)
            if i == 0:
                self.genome[i] = product
                self.genome[i + 1] = agent_id
            else:
                self.genome[i + 1] = product
                self.genome[i + 2] = agent_id

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
