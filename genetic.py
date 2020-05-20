import numpy as np 
from network import init,train
import random

no_of_generations = 10
no_of_individuals = 10
mutate_factor = 0.2
individuals = []

layers = [0, 3, 5]

def mutate(new_individual):

    for i in layers:
        for bias in new_individual.layers[i].get_weights()[1]:
            for j in range(len(bias)):
                if(random.uniform(0, 1) < mutate_factor):
                    new_individual.layers[i].get_weights()[1][j] *= random.choice(-0.5, 0.5)

    for i in layers:
        for weight in new_individual.layers[i].get_weights()[0]:
            for j in range(len(weight)):
                for k in range(len(weight[0])):
                    if(random.uniform(0, 1) < mutate_factor):
                        new_individual.layers[i].get_weights()[0][j][k] *= random.choice(-0.5, 0.5)


    return new_individual
    
                
                




def crossover(individuals):
    new_individuals = []

    new_individuals.append(individuals[0])
    new_individuals.append(individuals[1])

    for i in range(2, no_of_individuals):
        if(i < (no_of_individuals - 2)):
            if(i == 2):
                parentA = random.choice(individuals[:3])
                parentB = random.choice(individuals[:3])
            else:
                parentA = random.choice(individuals[:])
                parentB = random.choice(individuals[:])

            for i in layers:
                temp = parentA.layers[i].get_weights()[1]
                parentA.layers[i].get_weights()[1] = parentB.layers[i].get_weights()[1]
                parentB.layers[i].get_weights()[1] = temp

                new_individual = random.choice([parentA, parentB])
            
        else:
             new_individual = random.choice(individuals[:])

        #new_individuals.append(mutate(new_individual))
        new_individuals.append(new_individual)

    return new_individuals

        





def evolve(individuals, losses):
    sorted_y_idx_list = sorted(range(len(losses)),key=lambda x:losses[x])
    individuals = [individuals[i] for i in sorted_y_idx_list ]

    #winners = individuals[:6]

    new_individuals = crossover(individuals)

    return new_individuals




for i in range(no_of_individuals):
    individuals.append(init())

for generation in range(no_of_generations):
    individuals, losses = train(individuals)
    print(losses)

    individuals = evolve(individuals, losses)