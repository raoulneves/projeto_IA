from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual


class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = len(ind1.genome)
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        # Swap genes between cut points and create mappings
        mapping1 = {}
        mapping2 = {}

        for i in range(cut1, cut2 + 1):
            mapping1[ind2.genome[i]] = ind1.genome[i]
            mapping2[ind1.genome[i]] = ind2.genome[i]
            ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

        # Update the remaining genes to eliminate duplicates
        for i in range(0, cut1):
            gene = ind1.genome[i]
            while gene in mapping1:
                gene = mapping1[gene]
            ind1.genome[i] = gene

            gene = ind2.genome[i]
            while gene in mapping2:
                gene = mapping2[gene]
            ind2.genome[i] = gene

        for i in range(cut2 + 1, num_genes):
            gene = ind1.genome[i]
            while gene in mapping1:
                gene = mapping1[gene]
            ind1.genome[i] = gene

            gene = ind2.genome[i]
            while gene in mapping2:
                gene = mapping2[gene]
            ind2.genome[i] = gene

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"
