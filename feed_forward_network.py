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
		self.hidActivation = zeros((self.numOfHiddenNeuron, 1), dtype = float)
		self.outputActivation = zeros((self.numOfOutput, 1), dtype = float)


		#create neurons
		self.inputNeurons = zeros((self.numOfInput + 1, 1), dtype = float)
		self.hiddNeurons = zeros((self.numOfHiddenNeuron + 1, self.numOfHiddenLayer), dtype = float)
		self.outputNeurons = zeros((self.numOfOutput), dtype = float)

		#deltas of each layers
		self.hiddDelta = zeros((self.numOfHiddenNeuron), dtype = float)
		self.outputDelta = zeros((self.numOfOutput), dtype = float)

	def feed_forward(self, input):


	def sigmoid(self, input):

	def sum(self, input):

	def back_propergation(self, train):

	def output(self):
		return self.outputNeurons

