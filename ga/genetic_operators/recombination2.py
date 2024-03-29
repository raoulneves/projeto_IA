from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination


class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        cut = GeneticAlgorithm.rand.randint(0, ind1.num_genes - 1)
        # Swap genes up to the cut point and create a mapping
        mapping1 = {}
        mapping2 = {}

        for i in range(cut + 1):
            mapping1[ind2.genome[i]] = ind1.genome[i]
            mapping2[ind1.genome[i]] = ind2.genome[i]
            ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

        # Update the remaining genes to eliminate duplicates
        for i in range(cut + 1, len(ind1.genome)):
            gene = ind1.genome[i]
            while gene in mapping1:
                gene = mapping1[gene]
            ind1.genome[i] = gene

            gene = ind2.genome[i]
            while gene in mapping2:
                gene = mapping2[gene]
            ind2.genome[i] = gene


    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
