from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def save(self):
        pass

    def revalidate(self):
        pass

    def sequence(self):
        self.parse()
        self.validate()
        self.revalidate()
        self.save()

class StandardReport(Report):
    def __init__(self):
        print("standard report generation") 

    def parse(self):
        print("> parsing standard report")
    
    def validate(self):
        print("> validating standard report")

    def save(self): 
        print("> saving standard report")

class SpecialReport(Report):
    def __init__(self):
        print("special report generation")

    def parse(self):
        print("> parsing special report")
    
    def validate(self):
        print("> validating special report")
    
    def revalidate(self):
        print("> revalidating special report")

    def save(self): 
        print("> saving special report")

# class PDF(StandardReport): # explicit report initialization
#     pass

# class CSV(SpecialReport):
#     pass

# pdf_report = PDF()
# pdf_report.sequence()

# csv_report = CSV()
# csv_report.sequence()
    
class ReportFactory:
    @staticmethod
    def generate(choice: int) -> Report:
        match choice:
            case 1: return StandardReport()
            case 2: return SpecialReport()
            case _: raise Exception("invalid choice")

if __name__ == "__main__":
    report = ReportFactory() # user driven report initialization

    print("1. standard report  2. special report")

    try:
        choice = int(input("> "))
    except Exception as e:
        print(e)

    report1 = report.generate(choice)

    report1.sequence()