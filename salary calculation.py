basic_salary = float(input("Enter Basic Salary: "))
da = basic_salary * 0.10
hra = basic_salary * 0.20
pf = basic_salary * 0.05
gross_salary = basic_salary + da + hra
net_salary = gross_salary - pf
print("\n--- Salary Details ---")
print("Basic Salary:", round(basic_salary, 2))
print("DA (10%):", round(da, 2))
print("HRA (20%):", round(hra, 2))
print("PF (5%):", round(pf, 2))
print("Gross Salary:", round(gross_salary, 2))
print("Net Salary:", round(net_salary, 2))
