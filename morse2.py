#Getting file names and opening them.
newFile=input('Please enter a name file  :')
hand=open(newFile)
newFile2=input('Pelase enter another file name :')
hand2=open(newFile2)
fileemail1=list()
#Reading words.
for email in hand:
    email=email.strip()
    fileemail1.append(email)
fileemail2=list()

for em in hand2:
    em=em.strip()
    fileemail2.append(em)
#Counting words for lapping.
a=len(fileemail1)
b=len(fileemail2)
#Empty list for common words.
commonList=list()
if(a>b):
    for x in fileemail1:
        if x in fileemail2 and x not in commonList:
            commonList.append(x)
        else:
            continue

else:
    for y in fileemail2:
        if y in fileemail1 and y not in commonList:
            commonList.append(y)
        else:
           continue
#New file for writing common words in.
hand3=open('common.txt','a')

for po in commonList:
    hand3.writelines(po+'\n')
    
    
#Closing files.
hand.close()   
hand2.close()
hand3.close()
                  
          
        
            
        

