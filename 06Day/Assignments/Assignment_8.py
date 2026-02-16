class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def _financial_report(self):
        print(f"{self.name} Financial Report")

    def show_details(self):
        print(f"Company: {self.name}, Location: {self.location}")

class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def _policy_update(self):
        print(f"Policy Update for {self.emp_id}")

    def show_details(self):
        print(f"{self.emp_name} ({self.emp_id}) - {self.designation}")

class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_details(self):
        super().show_details()
        print("Merged Employees:")
        for employee in self.employees:
            employee.show_details()

class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joined: {self.joining_date}, Previous Company: {self.previous_company}")

class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size

    def access_financial_report(self, company): # giving access to private method _financial_report
        company._financial_report()

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled

    def access_policy_update(self, employee): # giving access to private method _policy_update
        employee._policy_update()

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")

class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages

    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {self.programming_languages}")

class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")

class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, policies_handled):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def access_financial_report(self, company):
        company._financial_report()

    def access_policy_update(self, employee):
        employee._policy_update()

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {', '.join(self.policies_handled)}")

company = CompanyAcquisition("VW", "BLR")

manager = Manager(123, "Abc", "Project Manager", "16-02-2026", "Z", 10)

hr = HR(234, "Xyz", "HR Manager", "15-02-2026", "Y", ["Recruitment", "Policies"])

developer = Developer(345, "Def", "SDE", "14-02-2026", "Y", ["Python", "Rust"])

intern = Intern(567, "Ghi", "Intern", "15-02-2026", "X", 6)

manager_hr = ManagerHR(789, "Jkl", "Manager", "10-02-2026", "W", 8, ["abcd", "efgh"])

company.add_employee(manager)
company.add_employee(developer)
company.add_employee(intern)
company.add_employee(manager_hr)

company.show_details()

# developer.access_financial_report(company) # should not work
manager.access_financial_report(company)
hr.access_policy_update(developer)

manager_hr.access_financial_report(company)
manager_hr.access_policy_update(intern)
