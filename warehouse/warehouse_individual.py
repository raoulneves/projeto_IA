from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.steps = 0
        self.path = []

    def compute_fitness(self) -> float:
        # TODO

        self.steps = 0
        self.fitness = 0
        agent = 0
        #current_agent = self.path[agent]
        agent_current_position = self.problem.agent_search.forklifts[agent]

        for i, gene in enumerate(self.genome):

            # Check if its 999
            if gene == 999:
                # AND if it is not the last gene
                if i+1 < len(self.genome):
                    if self.genome[i + 1] != 999 and self.genome[i + 1] is not None:
                        agent += 1
                        agent_current_position = self.problem.agent_search.forklifts[agent]
                        current_agent = self.path[agent]
                        continue
                    else:
                        continue
                else:
                    continue

            for pairs in self.problem.agent_search.pairs:
                if pairs.cell1 == agent_current_position and pairs.cell2 == self.problem.agent_search.products[gene]:
                    self.fitness += pairs.value
                    self.steps += len(pairs.solution)
                    current_agent.append(pairs.solution)
                    agent_current_position = self.problem.agent_search.products[gene]
                elif pairs.cell1 == self.problem.agent_search.products[gene] and pairs.cell2 == agent_current_position:
                    self.fitness += pairs.value
                    self.steps += len(pairs.solution)
                    current_agent.append(pairs.solution)
                    agent_current_position = self.problem.agent_search.products[gene]

        for pairs in self.problem.agent_search.pairs:
            if pairs.cell1 == agent_current_position and pairs.cell2 == self.problem.agent_search.exit:
                self.fitness += pairs.value
                self.steps += len(pairs.solution)
                current_agent.append(pairs.solution)
            elif pairs.cell2 == self.problem.agent_search.exit and pairs.cell2 == agent_current_position:
                self.fitness += pairs.value
                self.steps += len(pairs.solution)
                current_agent.append(pairs.solution)

        return self.fitness

    def obtain_all_path(self):
        # TODO

        forklift_path = []
        # Set starting position for each forklift, should look like this
        # forklift_path = [
        #     [Cell(line=0, column=0)],  # Initial path for forklift 1
        #     [Cell(line=1, column=1)]  # Initial path for forklift 2
        # ]
        for i, forklift in enumerate(self.problem.agent_search.forklifts):
            forklift_path[i].append(forklift)

        for step in range(self.steps):
            for i in range(len(forklift_path)):
                current_forklift = forklift_path[i]

                #for action in self.path:
                    #if action
                # Determine the current step to be added to the forklift's path
                #current_step = Cell(line=step, column=step)

                # Add the current step to the forklift's path
                #current_forklift.append(current_step)

                # Perform any necessary operations with the current_step and current_forklift

                # Print the current step and the updated forklift path
                #print(f"Step {step + 1}: Forklift {i + 1} path: {current_forklift}")

        # [[Cell(4, 4), Cell(4, 3), Cell(3, 3), Cell(2, 3), Cell(1, 3), Cell(1, 3), Cell(0, 3), Cell(0, 4)]], 7
        # [[Cell(4, 4), Cell(4, 3), Cell(3, 3), Cell(2, 3), Cell(1, 3), Cell(1, 3), Cell(0, 3), Cell(0, 4)],
        # [Cell(4, 4), Cell(4, 3), Cell(3, 3), Cell(2, 3), Cell(1, 3), Cell(1, 3), Cell(0, 3), Cell(0, 4)]], 7
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += "Genome: " + str(self.genome) + "\n"
        # TODO
        agent = 0
        for i, gene in enumerate(self.genome):
            # Agent updater
            if gene == 999:
                # AND if it is not the last gene
                if i + 1 < len(self.genome):
                    if self.genome[i + 1] != 999 and self.genome[i + 1] is not None:
                        agent += 1
                        continue
                    else:
                        continue
                else:
                    continue
            string += "Agent " + f"{agent+1}:\t" + str(gene+1) + "\n"

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
