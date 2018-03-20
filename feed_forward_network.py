import numpy as np

class feed_forward_network:

	def __init__(self, numOfInput, numOfHiddenNeuron, numOfHiddenLayer, numOfOutput):

		#setup learning rate
		self.epsilon = 0.05;

		#dimesion of each layer
		self.numOfInput = numOfInput + 1;#bias
		self.numOfHiddenNeuron = numOfHiddenNeuron + 1;
		self.numOfOutput = numOfOutput;


		#initialize weights
		self.hidWeights = 0.5;
		self.outputWeights = 0.5; 

		#activatoin functions or sigmoid
		self.hidActivation = zeros((self.numOfHiddenNeuron, self.numOfHiddenLayer), dtype = float)
		self.outputActivation = zeros((self.numOfOutput, 1), dtype = float)


		#create neurons
		self.inputNeurons = zeros((self.numOfInput + 1, 1), dtype = float)
		self.hiddNeurons = zeros((self.numOfHiddenNeuron + 1, self.numOfHiddenLayer), dtype = float)
		self.outputNeurons = zeros((self.numOfOutput), dtype = float)

		#deltas of each layers
		self.hiddDelta = zeros((self.numOfHiddenNeuron), dtype = float)
		self.outputDelta = zeros((self.numOfOutput), dtype = float)


	def feed_forward(self, input):
		#set input as the first layer of output and bias = 1
		self.inputNeurons[:-1, 0] = input
		self.inputNeurons[-1: 0] = 1.0

		#hidden layer
		self.hidActivation = self.sigmoid(self.hidWeights, self.inputNeurons)
		self.hiddNeurons = self.output(self.hidActivation)

		#set bias in hidden layer to 1
		self.hiddNeurons[-1:,:] = 1.0

		#output layer
		self.outputActivation = self.sigmoid(self.outputWeights, self.hiddNeurons)
		self.outputNeurons = self.output(self.outputActivation)

	def backpropagation(self, result):
		error = self.outputNeurons - array(result, dtype = float)

		#delta of output neurons
		self.outputDelta = (1 - tanh(self.outputActivation)) * tanh(self.outputActivation) * error

		#delta of hidden layers


		#aply weight changes
		#hidden layers

		#outputlayers
		self.outputWeights = self.outputWeights - self.epsilon * dot(self.outputDelta, self.hiddNeurons[:-1].transpose())


	def get_output(self):
		return self.outputNeurons


	def sigmoid(self, weights, output):

	def output(self, activation):

	def sum(self, input):

