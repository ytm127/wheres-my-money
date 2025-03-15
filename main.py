import argparse
import json
import time

class BudgetEngine():
    def __init__(self, data):
        self.cats = [
            ("FD", "food", 300),
            ("GR", "groceries", 500),
            ("MD", "medical stuff", 300),
            ("HS", "housing and utilities", 2050), 
            ("MS", "miscellaneous", 500), 
            ("SV", "savings", 0), 
            ("IV", "investments", 0), 
            ("HB", "hobbies", 300),
            ("TS", "transportation", 350),
            ("TR", "travel", 225),
            ("WD", "weed", 150),
            ("CH", "charity", 80),
            ("CF", "coffee", 75)
        ]
        self.dict_data = data
        self.new_items_count = 0


    def start(self):
        name = None
        price = None
        cat = None
        val = None
        
        # Get input about items
        while val != "x":
            print("=======================")
            print("Add item... (x to exit)")
            val = input("Name: ")
            if val == "x":
                continue
            name = val
            val = input("Price: ")
            while not isinstance(int(val), int):
                val = input("Invalid Price value. Try again... :  ")
            price = val
            for cat in self.cats:
                print(f"{cat[1]} --> {cat[0]}")
            val = input("Cat: ")
            while val not in [cat[0] for cat in self.cats]:
                print("Invalid Category value. Try again.")
                val = input("Cat:")
            cat = val
            
            # Add item to dict_data
            if name != None and price != None and cat != None:
                item = dict(name=name, price=price, category=cat, date=time.strftime("%Y-%m-%d"))
                self.dict_data[item["category"]].append(item)
                self.new_items_count += 1
                



if __name__ == "__main__":

    def read_json_file(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def print_summary(e):
        dt = time.strftime("%Y-%m-%d")
        data = e.dict_data
        print(f"""

            =================
            Spending so far this month

            {dt}
            =================

              """)
        total_budget = 0
        total_spend = 0
        for key in data.keys():
            dict_vals = data[key]
            total_so_far = sum([int(val["price"]) for val in dict_vals])
            cat_val = [cat for cat in e.cats if cat[0] == key][0]
            cat_name = cat_val[1].upper()
            cat_budget = cat_val[2]
            remaining = int(cat_budget) - int(total_so_far)

            total_budget += cat_budget
            total_spend += total_so_far
            
           # if remaining <= 0:
           #     print(f"            {key} -- [NO MORE FUNDS]  ${remaining}")
           # elif remaining < 50:
           #     print(f"            {key} -- [LOW]  ${remaining}")
           # else:
           #     print(f"            {key} -- ${remaining}")
            print(f"""               {cat_name}:   {total_so_far}  ({cat_budget}) 
            -------------------------------------""")
        print(f"""
            Total budget for the month is {total_budget}
            Total spend for the month is {total_spend}
            Current balance is {total_budget - total_spend}
              """)



    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Read a JSON file and print its contents.")
        parser.add_argument(
            "--file",
            required=True,
            help="Path to the JSON file."
        )
        args = parser.parse_args()
    
        data = read_json_file(args.file)
        
        e = BudgetEngine(data)
        e.start()
        print("=========================")
        
        if e.new_items_count < 1:
            pass
        else:
            with open(args.file, "w") as f:
                print(f"about to write {e.new_items_count} new items to the file")
                val = input("continue? (y/n)")
                if val == "y":
                    json.dump(e.dict_data, f, indent=4)

        print_summary(e)


