import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.B1 = np.random.randn(self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.B2 = np.random.randn(self.output_size)

    def sigmoid(self, s):
        # Activation function
        return 1 / (1 + np.exp(-s))

    def forward(self, X):
        # Forward propagation through the network
        self.z = np.dot(X, self.W1) + self.B1
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2) + self.B2
        o = self.sigmoid(self.z3)
        return o
    
    def mutate(self):
        # Mutate the weights and biases
        rate = np.random.uniform(-1, 1)
        self.W1 += np.random.randn(self.input_size, self.hidden_size) * rate
        self.B1 += np.random.randn(self.hidden_size) * rate
        self.W2 += np.random.randn(self.hidden_size, self.output_size) * rate
        self.B2 += np.random.randn(self.output_size) * rate

    def crossover(self, partner):
        # Crossover operation between two neural networks
        # Initialize child network with the same architecture
        child = NeuralNetwork(self.input_size, self.hidden_size, self.output_size)

        # Randomly select crossover point
        crossover_point1 = np.random.randint(self.input_size)
        crossover_point2 = np.random.randint(self.hidden_size)
        crossover_point3 = np.random.randint(self.output_size)

        # Perform crossover for the first layer
        child.W1[:crossover_point1, :] = self.W1[:crossover_point1, :]
        child.W1[crossover_point1:, :] = partner.W1[crossover_point1:, :]

        # Perform crossover for the first bias
        child.B1[:crossover_point2] = self.B1[:crossover_point2]
        child.B1[crossover_point2:] = partner.B1[crossover_point2:]

        # Perform crossover for the second layer
        child.W2[:, :crossover_point2] = self.W2[:, :crossover_point2]
        child.W2[:, crossover_point2:] = partner.W2[:, crossover_point2:]

        # Perform crossover for the second bias
        child.B2[:crossover_point3] = self.B2[:crossover_point3]
        child.B2[crossover_point3:] = partner.B2[crossover_point3:]

        return child

    