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





