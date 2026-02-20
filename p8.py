birthdays={'shivani':'may 11','myna':'nov 2'}
while True:
      print('Enter the name:(blank to quit)')
      name=input()
      if name=='':
          break
      if name in birthdays:
         print(birthdays[name]+'is birthday of'+name)
      else:
          print('i dont have birthday information for'+name)
          print('What is the birthday')
          bday=input()
          birthdays [name]=bday
          print('birthday database updated')
