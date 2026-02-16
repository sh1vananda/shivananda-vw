class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company: {self.name}, Location: {self.location}")

class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

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

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled

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
        print(f"Internship Duration: {self.duration}")

class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, policies_handled):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")

class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages, duration):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages
        self.duration = duration

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Programming Languages: {self.programming_languages}")
        print(f"Internship Duration: {self.duration}")


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
