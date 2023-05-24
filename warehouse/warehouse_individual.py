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

        # Iterate over all agents to calculate the steps and picked products
        for i, agent in enumerate(self.problem.agents_db):
            agent_id = agent[0]
            agent_pos = agent[1]
            agent_current_pos = None
            first_pass_flag = True

            # Iterate over all tasks in the GENOME to calculate the steps and picked products
            for j, task in enumerate(self.genome):
                product_tofetch_id = task[0]
                agent_fetcher_id = task[1]
                product_pos = None
                agent_retrieved_pos = None

                if agent_id == agent_fetcher_id:
                    # Retrieve the position of the product to fetch
                    for data in self.problem.products_db:
                        if data[0] == product_tofetch_id:
                            product_pos = data[1]
                            break

                    # Retrieve the position of the agent
                    for data in self.problem.agents_db:
                        if data[0] == agent_fetcher_id:
                            agent_retrieved_pos = data[1]
                            break

                    # Find the cost already calculated
                    for pairs in self.problem.pairs:
                        # If it's the first time, use starting position
                        if first_pass_flag:
                            if pairs.cell1 == agent_retrieved_pos and pairs.cell2 == product_pos:
                                self.steps += pairs.value
                                break
                        # If it's not the first time, use the last position
                        else:
                            if pairs.cell1 == agent_current_pos and pairs.cell2 == product_pos:
                                self.steps += pairs.value
                                break

                    agent_current_pos = product_pos

            # Find the cost to the exit
            for pairs in self.problem.pairs:
                if pairs.cell1 == agent_current_pos and pairs.cell2 == self.problem.exit:
                    self.steps += pairs.value
                    break

        print("Steps: ", self.steps)
        self.fitness = self.steps
        return self.steps

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
