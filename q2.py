#question 2: compute a person's income tax

gross_income=float(input("please enter gross income"))
standard_deduction=$10000
dependents=int(input("enter the no. of dependents:"))
#there is a $3000 deduction for each dependents
dependent_deduction=3000

#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("taxable income:")
print(taxable_income)
tax=(taxable_income*20)/100
print("tax:")
print(tax)
