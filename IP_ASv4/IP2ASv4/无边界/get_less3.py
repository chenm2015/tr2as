import operator
f2=open("AS_Dict","r")
f3=open("result_less3_tmp1.txt","w")
for k in f2:
    tmp1=k.split(':')
    l=0
    val=tmp1[1].split(',')
    #print tmp1[0]
    while 1:
        try:
            if int(val[l])>3:
                #print "hello",val[l]
                break
            else:
                #print "hello1"
                l=l+1
        except:
f = open ("result_less3_tmp1.txt","r")
f1 =open("result_less3_tmp2.txt","a")
for i in f:
    i=i.rstrip('\n')
    i=i.rstrip()
    tmp = i.split(':')
    f1.write(tmp[0]+":")
    tmp1 = tmp[1].split(',')
    tmp1.sort()
    myset = set(tmp1)
    for item in myset:
        f1.write(item+"("+str(tmp1.count(item))+")"+'  ')
    f1.write('\n')
f.close()
f1.close()
f2=open("result_less3.txt","a")
f3=open("result_less3_tmp2.txt","r")
D={}
k=0
m=0
n=0
for j in f3:
    tmp2=j.split(':')
    if tmp2[0].find("_")!=-1:
        f2.write(j)
    elif tmp2[0].find(";")!=-1:
	    f2.write(j)
    elif tmp2[0]=="None":
	    f2.write(j)
    elif tmp2[0]=="q":
	    f2.write(j)
    else:
        try:
            D[int(tmp2[0])]=tmp2[1]
            k=k+1
            print j
        except:
            break
#L.sort(key=operator.itemgetter(0))
sorted(D.keys())
for m in sorted(D.keys()):
    f2.write( str(m)+':'+D[m])
