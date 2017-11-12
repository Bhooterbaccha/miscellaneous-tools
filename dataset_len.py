import sys
inp_file = sys.argv[1]
out_file = sys.argv[2]
count = 0
#keep dataset length to some fixed value. Takes the first n lines from a file
f=open(sys.argv[1],'r')
fo = open(sys.argv[2],'w')
in_f=f.readlines()
for i in in_f:
	if count < 5000:
		fo.write(i)
		count = count+1
f.close()
fo.close()		
