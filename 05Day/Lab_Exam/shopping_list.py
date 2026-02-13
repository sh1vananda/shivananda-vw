""" Shivananda Reddy Kankanala """

import os

class ShoppingList:
    file = "shopping_list.txt"
    
    def __init__(self):
        self.items = {}
        self.load_items()

    def start_menu(self):
        print("""What do you want to add to your shopping list?
Enter "DONE" to stop adding items
Enter "HELP" for additional info
Enter "SHOW" to view shopping list
Enter "REMOVE" to remove a product
Enter "SEARCH" to search for items
Enter "CLEAR" clear list""")
        
    def parse_item(self, text):
        """ handle quantities """
        parts = text.strip().split("x")

        item_name = parts[0].strip().capitalize()

        item_quantity = 1

        if len(parts) > 1:
            item_quantity = int(parts[1].strip())
            if item_quantity <= 0:
                item_quantity = 1
        
        return item_name, item_quantity
        
    def add_to_list(self, text):
        name, quantity = self.parse_item(text)

        if not name:
            print("Item cannot be empty")
            return 
        if name in self.items:
            print(f"{name} already in list, update quantity?")
            choice = input("(Y/N): ")
            if choice.lower() == "y":
                self.items[name] += quantity
            else:
                print(f"{name} already in list, quantity not updated")
        else:
            self.items[name] = quantity
    
    def remove_item(self, name):
        name = name.strip().capitalize()

        if name in self.items:
            del self.items[name]
            print(f"{name} was removed from the list")
        else:
            print(f"{name} not in list")
    
    def clear_list(self):
        print("Are you sure you want to clear the list?")
        confirm = input("(Y/N): ")
        if confirm.lower() == "y":
            self.items.clear()
            print("shopping list cleared")
        else:
            print("cancelled")
    
    def search_item(self, term):
        term = term.lower()
        results = [name for name in self.items if term in name.lower()]
        
        if not results:
            print("No matching items found")
        else:
            print(f"Results for {term}: ")
            for item in sorted(results):
                qty = self.items[item]
                if qty > 1:
                    print(f"{item} x{qty}")
                else:
                    print(f"{item}")

    def show_shopping_list(self):
        print("My List: ")
        if not self.items:
            print("Empty")
            return
        for item in sorted(self.items):
            qty = self.items[item]
            if qty > 1:
                print(f"> {item} x{qty}")
            else:
                print(f"> {item}")
        
    def save_items(self):
        with open(self.file, "w") as f: # avoiding append mode to prevent duplicates on rerun
            for item in self.items:
                f.write(f"{item} | {self.items[item]}\n")

    def load_items(self):
        try:
            with open(self.file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("|")
                    name = parts[0].strip()
                    quantity = int(parts[1].strip()) if len(parts) > 1 else 1
                    self.items[name] = quantity
        except Exception as e:
            self.items = {}

# ---

def main():
    shopping_list = ShoppingList()
    shopping_list.start_menu()

    try:
        while True:
            command = input("> ").strip()
            if not command:
                continue
            cmd = command.upper()

            match cmd:
                case "DONE":
                    print("Exiting...")
                    print("See you soon")
                    break
                case "HELP":
                    shopping_list.start_menu()
                case "SHOW":
                    shopping_list.show_shopping_list()
                case "REMOVE":
                    shopping_list.show_shopping_list()
                    item = input("What do you want to remove: ")
                    shopping_list.remove_item(item)
                case "SEARCH":
                    term = input("Search for: ")
                    shopping_list.search_item(term)
                case "CLEAR":
                    shopping_list.clear_list()
                case _:
                    shopping_list.add_to_list(command)
    except Exception as e:
        print(f"{e}")
    finally:
        shopping_list.save_items()
        print(f"Shopping list saved to shopping_list.txt")

if __name__ =="__main__":
    main()