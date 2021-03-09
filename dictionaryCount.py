fileName=input('Please enter a file name :')
hand=open(fileName)
myDict=dict()

for line in hand:
    line=line.strip()
    words=line.split()
    for word in words:
        myDict[word]=myDict.get(word,0)+1

commonWord=''
count=-1

for k,v in myDict.items():
    if count ==-1 or v>count:
        commonWord=k
        count=v

print(sorted([ (v,k) for k,v in myDict.items()]))
'''       
a=list()
for k,v in myDict.items():
    b= (v,k)
    a.append(b)

b=list()
b=sorted(a,reverse=True)
print(b[5:10])
'''