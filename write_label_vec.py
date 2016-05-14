import word2vec

# model_en = word2vec.load('en_tokenized.bin')

# N, D = model_en.vectors.shape

# f_vec = open('en_wiki.vecs','w')
# f_lab = open('en_wiki.labels','w')

# for i in range(N):
# 	f_lab.write(model_en.vocab[i].encode("utf-8")+'\n')
# 	f_vec.write(' '.join(str(x) for x in model_en.vectors[0])+'\n')
# print i
# f_vec.close()
# f_lab.close()

import codecs

model_ch = word2vec.load('ch_tokenized.bin')

N, D = model_ch.vectors.shape

f_vec = open('ch_wiki.vecs','w')
f_lab = codecs.open('ch_wiki.labels','w+',encoding='utf-8')

for i in range(N):
	f_lab.write(model_ch.vocab[i]+'\n')
	f_vec.write(' '.join(str(x) for x in model_ch.vectors[0])+'\n')

f_vec.close()
f_lab.close()