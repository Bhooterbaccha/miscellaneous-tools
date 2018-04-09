from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
import os, sys, datetime, nltk, re, time

count = 0
list_of_sents = []
file = sys.argv[1]
out_file = sys.argv[2]
ofile = open(out_file,"w+")
def duplicacy_check(l_o):
	sent_parsed=[]
	for l in l_o:
		#print(l)
		urls = re.findall('https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', l)
		for url in urls:
			l=l.replace(str(url)," ")
		sent_parsed.append(l)
	return sent_parsed
def duplicacy_check_sent(sen):
	#print(sen)
	urls = re.findall('https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', sen)
	for url in urls:
			#print(url)
			sen=sen.replace(str(url)," ")
	#time.sleep(1)
	return sen		
	

with open(file,'r') as f:
	sents = f.readlines()
	#print(sents)
for line in sents:
	sentence = line.split(">>>>")
	if len(sentence[0]) > 3:
		list_of_sents.append(sentence[0])
print(str(len(list_of_sents))+":total no of sentences")
l_o_s = set(list_of_sents)
l_o = list(l_o_s)
print(str(len(l_o))+":no of sentences left after direct removal")
time.sleep(5)
sentences= duplicacy_check(l_o)
#print(l_o)




#print(sent_parsed)
sent_Set=set(sentences)
sents_orig =list(sent_Set)
#print(str(len(sents_orig))+" 2")
sent = []
#print(sents_orig)
for l1 in l_o:
	i=0
	cut_sent = str(duplicacy_check_sent(str(l1)))
	#print(cut_sent+">>>>>")
	cut_sent = cut_sent.rstrip()
	sent.append(cut_sent)
	#print(sent)
	for l in sent:
		#print(l+"****")
		#print(cut_sent+"****")
		if str(l) == cut_sent:
			i=i+1
			#print("duplcatr")
		#time.sleep(1)
	#print(i)	
	if i <= 1:
		#print("out")
		#print(l1)
		ofile.write(l1.rstrip()+"\n")
		count = count + 1

	

print(str(count)+":non duplicate sentences")				
#for l in l_o:
#	ofile.write(l+"\n")
ofile.close()			 
