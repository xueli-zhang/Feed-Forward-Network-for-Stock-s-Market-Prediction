import numpy as np

class feed_forward_network:

	def __init__(self, numOfInput, numOfHidden, numOfOutput):

		#setup learning rate
		self.epsilon = 0.05;

		#dimesion of each layer
		self.numOfInput = numOfInput + 1;#bias
		self.numOfHidden = numOfHidden + 1;
		self.numOfOutput = numOfOutput;


		#initialize weights
		self.hidWeights = 0.5;
		self.outputWeights = 0.5; 

		#activatoin functions or sigmoid
		self.hidActivation = zeros((self.numOfHidden, 1), dtype = float)
		self.outputActivation = zeros((self.numOfOutput, 1), dtype = float)


		#create neurons

		self.inputNeurons = zeros((self.numOfInput + 1, 1), dtype = float)
		self.hiddNeurons = zeros((self.numOfHidden + 1, 1), dtype = float)
		self.outputNeurons = zeros((self.numOfOutput), dtype = float)

		#deltas of each layers
		self.hiddDelta = zeros((self.numOfHidden), dtype = float)
		self.outputDelta = zeros((self.numOfOutput), dtype = float)

