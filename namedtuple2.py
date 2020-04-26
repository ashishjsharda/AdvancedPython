from collections import namedtuple
employee=namedtuple('Employee',['name','empid'])
emp_1=employee('Rick','201')
print(emp_1.name)
