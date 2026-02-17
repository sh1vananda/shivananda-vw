import time

def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"time: {end - start}")
        return res
    return wrapper

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        print("file is open")
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("file is closed")

class Report:
    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, num):
        for i in range(num):
            yield f"line {i + 1}"

    @logger
    def save(self, num):
        with FileManager(self.filename) as f:
            for line in self.generate(num):
                f.write(line + "\n")

report = Report("text.txt")
report.save(100)