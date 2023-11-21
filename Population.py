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
            self.population.append(Agent("Agent " + str(i),deck,dealer,NeuralNetwork(4, 5, 6)))

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


    def select_agents(self):
        total_fitness = sum(agent.fitness for agent in self.population)
        probabilities = [agent.fitness / total_fitness for agent in self.population]
        self.selected_agents = random.choices(self.population, weights=probabilities, k=PARENTS_SELECTED)
    
    def crossover_and_mutate(self):
        for i in range(POPULATION_SIZE - PARENTS_SELECTED):
            parent1 = random.choice(self.selected_agents)
            parent2 = random.choice(self.selected_agents)
            child = parent1.crossover(parent2)
            self.selected_agents.append(child)

        for i in range(POPULATION_SIZE):
            r = random.random()
            if r < MUTATION_RATE:
                self.selected_agents[i].mutate()
        self.population = self.selected_agents

    def next_gen(self):
        self.calculate_fitness()
        self.select_agents()
        self.crossover_and_mutate()
        self.generation += 1
