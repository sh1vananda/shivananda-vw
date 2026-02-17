# class Singleton:
#     _instance = None
    
#     def __new__(cls, *args, **kwargs):
#         if cls._instance == None:
#             cls._instance = super().__new__(cls)
#             print("instance created")
#         return cls._instance
    
#     def __init__(self, value):
#         self.value = value

# s1 = Singleton(10)
# print(s1.value)

# s2 = Singleton(20)

# print(s1.value, id(s1))
# print(s2.value, id(s2))

# print(s1 is s2)

# ---

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    
class MySQL(Database):
    def __init__(self):
        print("MySQL db created")
    def insert(self):
        print("MySQL - insert")
    def update(self):
        print("MySQL - update")
    def delete(self):
        print("MySQL - delete")

class Oracle(Database):
    def __init__(self):
        print("Oracle db created")
    def insert(self):
        print("Oracle - insert")
    def update(self):
        print("Oracle - update")
    def delete(self):
        print("Oracle - delete")

class Factory:
    @staticmethod
    def get_db(choice: int) -> str | Database:
        match choice:
            case 1: return MySQL()
            case 2: return Oracle()
            case _: raise Exception("invalid choice")
        
if __name__ == "__main__":
    try:
        db1 = Factory.get_db(1)
        db2 = Factory.get_db(2)
        db3 = Factory.get_db(3)
    except Exception as e:
        print(e)

    try:
        db1.insert()
        db2.insert()
        db3.insert()
    except Exception as e:
        print(e)