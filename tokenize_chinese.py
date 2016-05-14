#coding=utf-8
import codecs
f = codecs.open('text.xml','r', 'utf-8')
outf = codecs.open('ch_tokenized.txt','w','utf-8')
firstline = f.readline()
for line in f:
	if list(line)[0] != '<':
		outf.write(" ".join(line))

f.close()
outf.close()



