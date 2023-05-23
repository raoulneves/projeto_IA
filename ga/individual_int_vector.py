import random
from abc import abstractmethod

import numpy as np
from numpy.ma import copy

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual
import copy as copycopy


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO

        # ATTEMPT 2
        # self.genome = np.full(num_genes, False, dtype=bool)

        # ATTEMPT 1
        # A genome would look something like this: (Product ID, Agent ID)
        #
        # For instance, if you have 3 agents and 5 products, a genome could be represented as:
        #
        # [(1, 2), (2, 1), (3, 2), (4, 3), (5, 1)]
        #
        # In this genome:
        #
        #     Agent 2 will pick up product 1
        #     Agent 1 will pick up product 2
        #     Agent 2 will pick up product 3
        #     Agent 3 will pick up product 4
        #     Agent 1 will pick up product 5

        self.genome = np.full((num_genes, 2), 0, dtype=int)

        # Generate a list of tuples with the index and the forklift
        tuple_agent_list = [(i, forklift) for i, forklift in enumerate(self.problem.forklifts)]
        self.agents = tuple(tuple_agent_list)

        # Generate a list of tuples with the index and the product
        tuple_product_list = [(i, product) for i, product in enumerate(self.problem.products)]
        self.products = tuple(tuple_product_list)


    def initialize(self):
        # Create a deep copy of the list of products
        # INFO: ITS "COPYCOPY" BECAUSE COPY WAS ALREADY USED FOR SOMETHING ELSE!
        copied_list_products = list(copycopy.deepcopy(self.products))

        # Shuffle the copied list
        random.shuffle(copied_list_products)

        # Generate the genome by randomly assigning products to agents
        # genome = [(product, random.choice(agents)) for product in products]
        for i, (product_id, _) in enumerate(copied_list_products):
            print("------------------")
            print("Product: ", product_id)
            agent_id = random.choice(self.agents)[0]
            print("Agents: ", agent_id)
            self.genome[i] = [product_id, agent_id]

            print("Genome: ", self.genome[i])

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
