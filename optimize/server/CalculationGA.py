from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

start_time = datetime.now()

DIMENSIONS = 2
LOW, UP = -3, 14
ETA = 20.0

# Константы ГА:
POPULATION_SIZE = 100
P_CROSSOVER = 0.93
P_MUTATION = 0.1
MAX_GENERATIONS = 100
PENALTY_VALUE = 12.0

HALL_OF_FAME_SIZE = 20

#RANDOM_SEED = 1
#random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def randomPoint(LOW, UP):
  s = random.uniform(LOW, UP)
  return round(s, 2)

toolbox.register("randomPoint", randomPoint, LOW, UP)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.randomPoint, DIMENSIONS)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

def calculateFunction(individual):
  T1 = individual[0]
  T2 = individual[1]
  f = ((T2 - T1)**2 + 1 / 9 * (T1 + T2 - 10)**2) * 8
  return f,

toolbox.register("evaluate", calculateFunction)

def feasible(individual):
    T1 = individual[0]
    T2 = individual[1]
    return T1 + T2 <= 12

toolbox.decorate("evaluate", tools.DeltaPenalty(feasible, PENALTY_VALUE))
toolbox.register("select", tools.selTournament, tournsize = 2)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=LOW, up=UP, eta=ETA)
toolbox.register("mutate", tools.mutPolynomialBounded, low=LOW, up=UP, eta=ETA, indpb=1.0/DIMENSIONS)

def main():
    population = toolbox.populationCreator(n = POPULATION_SIZE)
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION, ngen=MAX_GENERATIONS, halloffame=hof, verbose=False)

    calculationTime = datetime.now() - start_time
    microseconds_GA = calculationTime.microseconds 

    bestIndividual = hof.items[0]
    T1_Ga = round(bestIndividual[0], 2)
    T2_Ga = round(bestIndividual[1], 2)
    maxFunction_GA = round(bestIndividual.fitness.values[0], 2)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize =(8, 10))

    X = np.linspace(LOW, UP, 60)
    Y = np.linspace(LOW, UP, 60)
    x, y = np.meshgrid(X, Y)
    z = ((y - x)**2 + 1 / 9 * (x + y - 10)**2) * 8

    ax.plot_surface(x, y, z, cmap='BuPu', cstride=1, rstride=1, edgecolor = 'royalblue', linewidth = 0.1, alpha=0.8)

    x_for_graph = [x[0] for x in population]
    y_for_graph = [x[1] for x in population]
    z_for_graph = [calculateFunction(x) for x in population]

    ax.scatter(x_for_graph, y_for_graph, z_for_graph, color = 'deeppink', marker='o', zorder=1)
    ax.view_init(20, 80)
    fig.savefig('GA.png', dpi=fig.dpi)
    open('GA.png','rb+')

    return [T1_Ga, T2_Ga, maxFunction_GA, microseconds_GA]
