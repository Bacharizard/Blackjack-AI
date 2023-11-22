from NeuralNetwork import NeuralNetwork
import numpy as np
import math
from Dealer import Dealer
from Deck import Deck
from Player import Player
from Hand import Hand
from GameLogic import GameLogic
from Agent import Agent
import random

POPULATION_SIZE = 100  
TRAINING_ROUNDS = 100
MUTATION_RATE = 0.1
PARENTS_SELECTED = 50

class Population:

    def __init__(self):
        self.population = []
        self.selected_agents = []
        self.generation = 1
        self.best_agent = None
        self.best_fitness = -1
        for i in range(POPULATION_SIZE):
            deck = Deck()
            dealer = Dealer(deck)
            self.population.append(Agent(deck,dealer,NeuralNetwork(4, 8, 6)))

    def calculate_fitness(self):
        self.best_fitness = -1
        for agent in self.population:
            agent.hands_played = 0
            agent.money = 1000
            for i in range(TRAINING_ROUNDS):
                if(agent.money >= 1):
                    agent.play_round()
                    agent.hands_played += 1
            agent.fitness = 0.8 * agent.money + 0.2 * agent.hands_played
            if agent.fitness > self.best_fitness:
                self.best_fitness = agent.fitness
                self.best_agent = agent

        
    
    def crossover_and_mutate(self):
        parents = self.population[:PARENTS_SELECTED]
        for i in range(PARENTS_SELECTED,POPULATION_SIZE-PARENTS_SELECTED):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = parent1.crossover(parent2)
            self.population[i] = child

        for i in range(POPULATION_SIZE):
            r = random.random()
            if r < MUTATION_RATE:
                self.population[i].mutate()

    def next_gen(self):
        self.calculate_fitness()
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        self.crossover_and_mutate()
        self.generation += 1
