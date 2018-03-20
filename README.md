Build A Feed Forward Network

Usage:

create ann: ann = feed_forward_network( int numOfInput, int numOfHiddenNeuron, int numOfHiddenLayer, int numOfOutput)

train ann: ann.feed_forward(traningDataset), ann.backpropagation(trainingDataset)

testing ann: ann.feed_forward(testingDataset), compare ann.ann_output()[0] with threshhold to get answer

example:

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