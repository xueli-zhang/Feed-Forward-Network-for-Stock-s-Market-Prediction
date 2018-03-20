from numpy import *
 
class feed_forward_network:

	def __init__(self, numOfInput, numOfHiddenNeuron, numOfHiddenLayer, numOfOutput):
		# learning rate
		self.epsilon = 0.05

		#dimesion of each layer
		self.numOfInput = numOfInput
		self.numOfHiddenNeuron = numOfHiddenNeuron
		self.numOfOutput = numOfOutput

		# initialize weights randomly (+1 for bias)
		self.hidWeights = random.random((self.numOfHiddenNeuron, self.numOfInput + 1))
		self.outputWeights = random.random((self.numOfOutput, self.numOfHiddenNeuron + 1))

		# activations of neurons (sum of inputs)
		self.hidActivation = zeros((self.numOfHiddenNeuron, 1), dtype=float)
		self.outputActivation = zeros((self.numOfOutput, 1), dtype=float)

		# outputs of neurons (after sigmoid function)
		self.inputNeurons = zeros((self.numOfInput + 1, 1), dtype=float)      # +1 for bias
		self.hiddNeurons = zeros((self.numOfHiddenNeuron + 1, 1), dtype=float)  # +1 for bias
		self.outputNeurons = zeros((self.numOfOutput), dtype=float)

		# deltas for hidden and output layer
		self.hiddDelta = zeros((self.numOfHiddenNeuron), dtype=float)
		self.outputDelta = zeros((self.numOfOutput), dtype=float)   


	def feed_forward(self, input):

		#set input as the first layer of output and bias = 1
		self.inputNeurons[:-1, 0] = input
		self.inputNeurons[-1:, 0] = 1.0

		#hidden layer
		self.hidActivation = dot(self.hidWeights, self.inputNeurons)
		self.hiddNeurons[:-1, :] = tanh(self.hidActivation)

		#set bias in hidden layer to 1
		self.hiddNeurons[-1:, :] = 1.0

		#output layer
		self.outputActivation = dot(self.outputWeights, self.hiddNeurons)
		self.outputNeurons = tanh(self.outputActivation)

	def backpropagation(self, result):
		error = self.outputNeurons - array(result, dtype = float)

		#delta of output neurons
		self.outputDelta = (1 - tanh(self.outputActivation)) * tanh(self.outputActivation) * error

		#delta of hidden layers
		self.hiddDelta = (1 - tanh(self.hidActivation)) * tanh(self.hidActivation) * dot(self.outputWeights[:,:-1].transpose(), self.outputDelta)


		#aply weight changes
		#hidden layers
		self.hidWeights = self.hidWeights - self.epsilon * dot(self.hiddDelta, self.inputNeurons.transpose())

		#outputlayers
		self.outputWeights = self.outputWeights - self.epsilon * dot(self.outputDelta, self.hiddNeurons.transpose())


	def ann_output(self):
		return self.outputNeurons


	def sigmoid(self, weights, output):
		return dot(weights, output)

	def output(self, activation):
		return tanh(activation)

if __name__ == '__main__':

	print ("training")
	#train set
	example = [[0,0],[0,1],[1,0],[1,1]]
	expected = [[0], [1], [1], [0]]

	ann = feed_forward_network(2, 2, 1, 1)

	count = 0
	correctness = 0

	correcP = 0
	print('start training: ')
	while(count <= 20000):
		#training
		i = random.randint(0,3)
		ans = 0
		ann.feed_forward(example[i])
		ann.backpropagation(expected[i])

		print (count, example[i], expected[i], ann.ann_output()[0])
		if ann.ann_output()[0] > 0.9:
			print ('TRUE')
			ans = 1
		elif ann.ann_output()[0] < 0.3:
			print ('FALSE')
			ans = 0
		if expected[i][0] == ans:
			correctness += 1
		count += 1
		correcP = (correctness / count)
		print ('correctness: ', correctness)
		print ('epoch: ', count)
		print ('correct percentage: ', correcP)

	print ('done training')
	print ('testing [0, 0], expected: FALSE')

	ann.feed_forward(example[0])
	if ann.ann_output()[0] > 0.9:
		print ('TRUE')			
	elif ann.ann_output()[0] < 0.3:
		print ('FALSE')


