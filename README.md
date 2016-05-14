# wanyili-finalproject
# Word vectors accross languages using deep neural nets

## Project submission

Please read the following to see what files are included in this repository and where you should look:

Please read [Project Report (pdf)](https://github.com/wellesleynlp/wanyili-finalproject/blob/master/project_report.pdf) to read the final project report written in LaTex.

Please see [wordvec_sentiment.ipynb](https://github.com/wellesleynlp/wanyili-finalproject/blob/master/wordvec_sentiment.ipynb) to see the Stanford CS224d assignment one that I have completed.

[Tokenize_chinese.py](https://github.com/wellesleynlp/wanyili-finalproject/blob/master/tokenize_chinese.py) is what I wrote to simply add a space after all the Chinese characters so that the file will be ready to feed into word2vec for training.

[Training.ipynb](https://github.com/wellesleynlp/wanyili-finalproject/blob/master/training.ipynb) use the word2vec Python wrapper to train both English and Chinese wikipedia data using neural network.

[Trained_models.ipynb](https://github.com/wellesleynlp/wanyili-finalproject/blob/master/trained_models.ipynb) is a small showcase to see what neural network does. I included examples closest words/characters to the same meaning words/character in English and Chinese. Please see the file for demonstration.

## Project Update

My NLP final project on word to vectors using deep neural nets.

In the past couple of weeks, I have been learning through the Stanford CS224d Deep Learning for NLP's online course site. So far, I have completed watching one third of semester worth of videos which touched topic mostly on neural net basics and work to vector methods (Skipgram and CBOW). I have also been reading papers and websites on Restricted Boltzmann Machines.

My goal of Milestone 1 is to not only complete a large portion of learning, reading and watching online course videos, but also to identify specfic tasks to complete. I have started and completed half of the course assignment 1 of the Stanford CS224d using iPython Notebook. I have completed coding sections and theoretical questions on softmax function, sigmoid function, gradient check function and a basic forward and backward propagation neural nets. Since this course has only 3 coding assignments, each one is very long and half of the assignment is about the equivalent length of one of our CS349 assignment.

My eventual goal is to complete one more large section on this Stanford CS224d assignment on word2vec and to attempt a small project using word2vec across two languages (English and Chinese). The project will be using corpus from wikipedia and I hope to visualize the word2vecs of two languages to see if through some phase shift/coordinates normalization, we can find any similarity between words that share the same meanings. Similar projects has done on comparing different latin laguages (English, Spanish, French and German. See Faruqui etc (http://www.cs.cmu.edu/~mfaruqui/papers/eacl14-vectors.pdf). This project is particularly interesting to me because I understand both languges but they are drastically different. In Chinese, the unit is not word but rather characters. Certain Chinese chracters have the meaning of English words, while others have to be used together to become a word.

I want to spend most of the time for this final project on understanding the theories behind the neural nets and once I have a good understanding, I want to attempt to do the project on word2vecs on multilanguages. The difficulties mainly lie in solving the Stanford CS224d assignment with no help: the solution is not given and the concepts are had to understand directly from watching the videos.

Reference:

* Google word2vec in C;
* word2vec Python wrapper (https://github.com/danielfrg/word2vec/blob/master/examples/word2vec.ipynb);
* Dumps.wikimedia (Chinese: https://dumps.wikimedia.org/zhwiki/20160407/zhwiki-20160407-pages-articles.xml.bz2; English: thanks for Sravana)
* Wikiextractor.py (https://github.com/bwbaugh/wikipedia-extractor)
* Stanford CS244d assignment 1
* Explain word2vec: http://deeplearning4j.org/word2vec



