'''print('Enter the name of the student')
student_name=input()
print('Enter the USN')
USN=input()
print('marks in three subjects are')
m1=int(input())
m2=int(input())
m3=int(input())
total_marks=m1+m2+m3
perc=(total_marks/300)*100
print('The name of the student is:',student_name)
print('USN number is:',USN)
print('first subject marks:',int(m1))
print('second subject marks:',int(m2))
print('third subject marks:',int(m3))
print ('Total marks of the student is:',int(total_marks))
print('percentage of the student is:',float(perc))
if perc>=75:
    division='first class with distinction'
elif perc>=60:
    division='first class'
elif perc>=40:
    division='pass'
else:
    division='fail'
print('class obtainted:',division)'''




'''import datetime
print('Enter the name')
name=input()
print('Enter the year of birth')
year=int(input())
curyear=datetime.datetime.today().year
age=curyear-year
if age>=60:
    print('the person is senior citizen:',age)
else:
    print('the person is not senior citizen:',age)'''
