import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.mutation import Mutation
from ga.individual import Individual


class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: Individual) -> None:
        # INSERTION mutation
        num_genes = len(ind.genome)

        # Select a random gene position to be moved
        gene_pos = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        # Select a random position to insert the gene
        insert_pos = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        # Extract the gene from the genome
        gene = ind.genome[gene_pos]
        # Remove the gene from its original position
        ind.genome = np.delete(ind.genome, gene_pos)
        # Insert the gene at the new position
        ind.genome = np.insert(ind.genome, insert_pos, gene)

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
