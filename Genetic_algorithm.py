import random

#MAX_GEN = 500
GEN_SIZE = 300
MAX_STABLE = 500

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def getCost(self, u, v):
        for edge in self.graph:
            if (edge[0]==u and edge[1]==v) or (edge[0]==v and edge[1]==u):
                return edge[2]

class Chromosome:

    def findCost(self, map):
        cost = 0
        for i in range(len(self.path)-1):
            cost = cost + map.getCost(self.path[i], self.path[i+1])
        return cost

    def __init__(self, path, map):
        self.path = path
        self.cost = self.findCost(map)

class Population:
    def __init__(self):
        self.chromoList = []

    def addChromosome(self, individual):
        self.chromoList.append(individual)
        self.chromoList.sort(key = lambda x: x.cost)

    def findBest(self):
        return self.chromoList[0]

    def findWorst(self):
        return self.chromoList[len(self.chromoList)-1]

    def findRandom(self):
        return self.chromoList[random.randint(2, len(self.chromoList)-1)]

def Selection(p, p_best = 0.1, p_worst = 0.1, p_rand = 0.8):
    selected_paths = []
    
    p_vals = random.choices([1,2,3], cum_weights=(p_best, p_worst, p_rand), k=GEN_SIZE)

    for val in p_vals:
        if val == 1:
            selected_paths.append(p.findBest())
        elif val == 2:
            selected_paths.append(p.findWorst())
        else:
            selected_paths.append(p.findRandom())

    return selected_paths

def CrossOver(p, selected_paths, g):
    cross_paths = []
    
    for i in range(GEN_SIZE):
        parents = random.sample(selected_paths, 2)

        geneA = random.randint(1, len(parents[0].path)-2)
        geneB = random.randint(1, len(parents[1].path)-2)

        start_gene = min(geneA, geneB)
        end_gene = max(geneA, geneB)

        new_path_1 = []
        new_path_2 = []

        for i in range(start_gene, end_gene):
            new_path_1.append(parents[0].path[i])
        new_path_2 = [vertex for vertex in parents[1].path if (vertex not in new_path_1 and vertex != 0)]
        new_path = new_path_1 + new_path_2

        new_path.insert(0, 0)
        new_path.append(0)

        c = Chromosome(new_path, g)
        p.addChromosome(c)

        cross_paths.append(c)

    return cross_paths

def Mutation(p, cross_paths, g, p_swap = 0.1):
    mutate_paths = []

    for i in range(GEN_SIZE):
        sibling = random.sample(cross_paths, 1)
        new_path = sibling[0].path.copy()

        while(random.random() > p_swap):
            swapA = random.randint(1, len(sibling[0].path)-2)
            swapB = random.randint(1, len(sibling[0].path)-2)

            temp = new_path[swapA]
            new_path[swapA] = new_path[swapB]
            new_path[swapB] = temp
        
        c = Chromosome(new_path, g)
        p.addChromosome(c)

        mutate_paths.append(c)

    return mutate_paths

def nextGeneration(selected_paths, cross_paths, mutate_paths, p_select = 0.1, p_cross = 0.6, p_mutate = 0.4):
    new_gen = []

    p_vals = random.choices([1,2,3], cum_weights=(p_select, p_cross, p_mutate), k=GEN_SIZE)

    for val in p_vals:
        if val == 1:
            new_gen.append(random.choice(selected_paths))
        elif val == 2:
            new_gen.append(random.choice(cross_paths))
        else:
            new_gen.append(random.choice(mutate_paths))

    return new_gen

if __name__ == '__main__':
    
    #Initialization

    #Graph
    g = Graph(50)
    for i in range(49):
        for j in range(i+1, 50):
            g.addEdge(i, j, random.randint(1,10))

    #Population
    p_init = Population()
    generation = 0

    #Chromosomes
    for i in range(GEN_SIZE):
        path = random.sample(range(1, g.V), g.V-1)
        path.insert(0, 0)
        path.append(0)

        c = Chromosome(path, g)
        p_init.addChromosome(c)

    #Selection
    selected_paths = Selection(p_init)

    #Cross Over
    cross_paths = CrossOver(p_init, selected_paths, g)

    #Mutation
    mutate_paths = Mutation(p_init, cross_paths, g)

    best = p_init.findBest()
    stable = 0

    #Repeat
    while stable < MAX_STABLE:
        #Update 
        print('Generation: ', generation)
        print('Best Cost: ', best.cost)
        print()
        
        #Initialize New Generation

        #Population
        p_new = Population()
        generation = generation + 1

        #Chromosomes
        new_chromosomes = nextGeneration(selected_paths, cross_paths, mutate_paths)
        for chromosome in new_chromosomes:
            p_new.addChromosome(chromosome)

        #Selection
        selected_paths = Selection(p_new)

        #Cross Over
        cross_paths = CrossOver(p_new, selected_paths, g)

        #Mutation
        mutate_paths = Mutation(p_new, cross_paths, g)

        cur_best = p_new.findBest()
        
        if cur_best.cost < best.cost:
            best = cur_best
            stable = 0
        else:
            stable = stable + 1
    
    print('Solution: ', best.path)
    print('Cost: ', best.cost)