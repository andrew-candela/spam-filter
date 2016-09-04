import glob, re
import random
import filter_functions as ff 

path='./spam_corpus/*/*'

data=[]

for fn in glob.glob(path):
	is_spam = "ham" not in fn

	with open(fn,'r') as file:
		for line in file:
			if line.startswith("Subject:"): # remove the leading "Subject: " and keep what's left
				subject = re.sub(r"^Subject: ", "", line).strip()
				data.append((subject, is_spam))

#now I have an array of tuples with (subject text, is spam).
#I need to partition this into a training set and then an evaluation set

def split_array(array,proportion_train):
	results=[],[]
	for row in data:
		results[0 if random.random() < proportion_train else 1].append(row)
	return results

train_data,test_data=split_array(data,0.75)

classifier = ff.NaiveBayesClassifier()
classifier.train(train_data)
example_string='Earn free money!'
prob=classifier.classify(example_string)
print("Now that we've trainied our model, we can assign a probability that a string is spam. For example '{}' is spam with probability {}.".format(example_string,prob))
