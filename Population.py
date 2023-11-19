import NeuralNetwork as NN
import numpy as np
import random
import Dealer as Dealer
import Player as Player
import Deck as Deck
import Hand as Hand
import Card as Card

POPULATION_SIZE = 100
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.5    

class Population:

    def __init__(self):
        self.population = []
        self.generation = 0
        self.best_fitness = 0
        self.best_nn = None
        for i in range(POPULATION_SIZE):
            self.population.append(NN.NeuralNetwork(4, 5, 6))
