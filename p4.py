num=input('Enter the number:')
print('The number entered is:',num)
uniqdig=set(num)
print(uniqdig)
for elem in uniqdig:
    print(elem,"occurs",num.count(elem),"times")
