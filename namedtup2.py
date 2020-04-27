from collections import namedtuple
student=namedtuple('Student',['name','rno'])
stud=student('Rohan','20')
print(stud.name)
print(stud.rno)
