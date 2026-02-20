
'''import operator
fname=input('Enter the file name:')
fp=open(fname,'r')
list={}
for line in fp:
    for word in line.split():
        if word in list:
            list[word]+=1
        else:
            list[word]=1
print('\n\n All words occurence before sorting\n')
print(str(list))
sorted_list=dict(sorted(list.items(),key=operator.itemgetter(1),reverse=True)[1:10])
print('\n\n sorted list of 10 words occurence from higher to lower\n')
print(str(sorted_list))'''



'''with open('s.txt.txt','r')as file:
          lines=file.readlines()
lines=[line.strip() for line in lines]
lines.sort()
with open('sorted_output.txt.txt','w')as file:
    for line in lines:
        file.write(line+'\n')
print("The contents have been sorted& written to 'sorted_output.txt'")'''
