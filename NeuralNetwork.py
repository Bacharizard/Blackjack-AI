import tensorflow as tf

class NeuralNetwork(tf.keras.Model):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()

        # Define the layers of your neural network
        self.dense1 = tf.keras.layers.Dense(128, activation='relu', input_shape=(input_size,))
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.output_layer = tf.keras.layers.Dense(output_size, activation='softmax')

    def call(self, inputs):
        # Define the forward pass
        x = self.dense1(inputs)
        x = self.dense2(x)
        return self.output_layer(x)
