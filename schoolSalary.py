def salary_schedule(starting_salary, percentage_increase, years_taught):
    print("Year\tSalary") 
    for year in range(1, years_taught + 1):
        salary = starting_salary * (1 + (percentage_increase / 100) * (year - 1))
        print(year, "\t", "${:,.2f}".format(salary))

starting_salary = 30000
percentage_increase = 2
years_taught = 10

salary_schedule(starting_salary, percentage_increase, years_taught)
