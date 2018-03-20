Build A Feed Forward Network

Usage:

create ann: ann = feed_forward_network( int numOfInput, int numOfHiddenNeuron, int numOfHiddenLayer, int numOfOutput)

train ann: ann.feed_forward(traningDataset), ann.backpropagation(trainingDataset)

testing ann: ann.feed_forward(testingDataset), compare ann.ann_output()[0] with threshhold to get answer 