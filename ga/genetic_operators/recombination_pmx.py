from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm


class RecombinationPMX(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        mapping1 = {}
        mapping2 = {}
        for i in range(cut1, cut2 + 1):
            mapping1[tuple(ind1.genome[i])] = tuple(ind2.genome[i])
            mapping2[tuple(ind2.genome[i])] = tuple(ind1.genome[i])

        child1 = [-1] * num_genes
        child2 = [-1] * num_genes

        # Copy the selected segment from ind1 to child1
        child1[cut1:cut2+1] = ind1.genome[cut1:cut2+1]

        # Copy the selected segment from ind2 to child2
        child2[cut1:cut2+1] = ind2.genome[cut1:cut2+1]

        # Fill in the remaining genes for child1
        for i in range(num_genes):
            if child1[i] == -1:
                gene = ind2.genome[i]
                while tuple(gene) in mapping1:
                    gene = mapping1[tuple(gene)]
                child1[i] = gene

        # Fill in the remaining genes for child2
        for i in range(num_genes):
            if child2[i] == -1:
                gene = ind1.genome[i]
                while tuple(gene) in mapping2:
                    gene = mapping2[tuple(gene)]
                child2[i] = gene

        ind1.genome = child1
        print("child1: ", child1)
        ind2.genome = child2
        print("child2: ", child2)

    def __str__(self):
        return "PMX recombination (" + f'{self.probability}' + ")"
