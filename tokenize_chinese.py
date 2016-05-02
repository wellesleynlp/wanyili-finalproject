#coding=utf-8

f = open('chinese.txt','r')
l = list(u"中文")
print l
for w in l:
	print w.decode('unicode-escape')