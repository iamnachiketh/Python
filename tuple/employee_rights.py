access_rights = input("Enter the employees with access rights (comma-separated): ").split(", ")
current_employees = input("Enter the current employees (comma-separated): ").split(", ")

access_set = {emp.lower() for emp in access_rights}
current_set = {emp.lower() for emp in current_employees}

access_set.intersection_update(current_set)

updated_access_rights = [emp for emp in access_rights if emp.lower() in access_set]

print("\nUpdated Access Rights List:")
for emp in sorted(updated_access_rights):
    print(emp)