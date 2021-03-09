#get two file names.
a=input("Enter name of  first file:")
b=input("Enter name of second file:")
#opening files.
file1=open(a)
file2=open(b)

#List 1 for file 1
firslist=list()
for letter in file1:
    letter=letter.strip()
    list1=letter.split()
    for a in list1:
        firslist.append(a)


#List 2 for file 2
secondlist=list()
for letter in file2:
    letter=letter.strip()
    list2=letter.split()
    for b in list2:
        secondlist.append(b)        
        
#List 3 for common words.
commonList=list()

l1=len(firslist)
l2=len(secondlist)

if l1>l2:
    for k1 in secondlist:
        if k1 in firslist and k1 not in commonList:
            commonList.append(k1)
        else:
            continue  

else:
    for k2 in firslist:
        if k2 in secondlist and k2 not in commonList:
            commonList.append(k2)
        else:
            continue  

print(commonList)        