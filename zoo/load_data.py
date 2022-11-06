import json
  
f = open('zoo/zoo_data/animals.json')
animals_data = json.load(f)
f.close()

f = open('zoo/zoo_data/employees.json')
employees_data = json.load(f)
f.close()

f = open('zoo/zoo_data/supplies.json')
supplies_data = json.load(f)
f.close()