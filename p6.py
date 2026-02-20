'''num=int(input('Enter the fibonaci sequence length:'))
first_term=0
second_term=1
print("the fibannoci series with",num,"terms are:")
print(first_term,second_term,end="")
for i in range(2,num):
    cur_term=first_term+second_term
    print(cur_term,end="")
    first_term=second_term
    second_term=cur_term'''




'''def fact(num):
 if num==0:
   return 1
 else:
     return num*fact(num-1)
n=int(input('Enter the value of N:'))                                         
r=int(input('Enter the value of R:'))
if r<0 or r>n:
   print("the value of r printed is wrong")
nCr=fact(n)//(fact(r)*fact(n-r))
print(n,'C',r,"=","%d"%nCr,sep="")'''                                       


'''class complex:
    def initcomplex(self):
        self.realpart = int(input('Enter the real part:'))
        self.imgpart = int(input('Enter the imaginary part:'))
    def display(self):
        print(self.realpart,"+",self.imgpart,"i",sep="")
    def sum(self,c1,c2):
        self.realpart = c1.realpart+c2.realpart
        self.imgpart = c1.imgpart+c2.imgpart
c1=complex()
c2=complex()
c3=complex()
print('Enter first complex number')
c1.initcomplex()
print('First complex number',end="")
c1.display()
print('Enter second complex number')
c2.initcomplex()
print('second complex number',end="")
c2.display()
print("sum of two complex numbers is",end="")
c3.sum(c1,c2)
c3.display()'''


         



      

