company_employees = {
    "Engineering" : {
        "Alice" :{"age" : 30 , "role" : "software engineer"},
        "Bob" : {"age" : 28 , "role" : "DevOps Engineer"}
    },
    "Hr" : {
        "Charlie" : {"age" : 35 , "role" : "HR Manager"}
    }

}
print(company_employees)
company_employees["Engineering"]["David"] = {"age" : 27 , "role" : "Data Scientist"} 

def count(company_employees):
 total_employees=0
 for departments , employees in company_employees.items():
    total_employees += len(employees)
 return total_employees

total = count(company_employees)
print("Total nb of employees :" , total)

def reverse_dictionary(input_dict):
  reversed_dict = {}
  for name , number in input_dict.items():
    if number not in reversed_dict:
      reversed_dict[number].append(name)
    return reversed_dict
  input_dict = {"Alice": 10 , "Bob" : 20 , "Charlie" : 10,"David" : 30}
  output_dict = reverse_dictionary(input_dict)
  print(output_dict)

