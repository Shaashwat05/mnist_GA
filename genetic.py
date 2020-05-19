import numpy as np 
from network import init,train
import random

no_of_generations = 10
no_of_individuals = 10
mating_factor = 0.8
individuals = []

def mutate(new_individuals):



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

            temp = parentA.layers[-1].get_weights()[1]
            parentA.layers[-1].get_weights()[1] = parentB.layers[-1].get_weights()[1]
            parentB.layers[-1].get_weights()[1] = temp

            new_individuals.append(random.choice(parentA, parentB))
            
        else:
             new_individuals.append[random.choice(individuals[:])]

    new_individuals = mutate(new_individuals)

    return new_individuals

        





def evolve(individuals, losses):
    individuals = [x for _,x in sorted(zip(losses,individuals))]
    #winners = individuals[:6]

    new_individuals = crossover(individuals)

    return new_individuals




for i in range(no_of_individuals):
    individuals.append(init())

for generation in range(no_of_generations):
    individuals, losses = train(individuals)

    individuals = evolve(individuals, losses)