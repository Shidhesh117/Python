import math
N=int(input('Enter the number of elements in the list:'))
numbers=[]
for i in range(N):
    num=float(input(f"Enter number{i+1}:"))
    numbers.append(num)
mean=sum(numbers)/N
sum=0
for x in numbers:
    sum=sum+(x-mean)**2
variance=sum/N
sd=math.sqrt(variance)
print('The given list of numbers is:',numbers)
print('The mean is:',mean)
print('The variance is:',format(variance,'2f'))
print('The standard deviation is:',format(sd,'2f'))
