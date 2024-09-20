from collections import defaultdict

employees = [
  ('Alice', 'Enginnering'),
  ('Bob', 'HR'),
  ('Charlie', 'Enginnering'),
  ('Dave', 'Finance'),
  ('Eve', 'HR'),
  ('Frank', 'Enginnering'),
  ('Grace', 'Finance'),
  ('Helen', 'Enginnering'),
  ('Ivan', 'HR')
]

# Utilizadno defaultdict
departament_groups = defaultdict(list)
for name,  department in employees:
  departament_groups[department].append(name)

print(departament_groups) 


# Utilizando regular dict
departament_groups = {}
for name, department in employees:
  if department in departament_groups:
    departament_groups[department].append(name)
  else:
    departament_groups[department] = [name]

# print(departament_groups)
