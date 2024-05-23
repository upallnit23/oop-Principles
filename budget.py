#Encapsulation in Personal Budget Management
#Task 1: Define Budget Category Class

"""class BudgetCategory:
    def __init__(self, catname, allbudget):
        self.__catname = catname
        self.__allbudget = allbudget
#Task 2:Implement Getters and Setters
    def get_catname(self):
        return self.__catname
    
    def get_allbudget(self):
        return self.__allbudget

    def set_catname(self, new_catname):
        self.__catname = new_catname

    def set_allbudget(self, new_allbudget):
        if new_allbudget >= 0:
            self.allbudget = new_allbudget
        else:
            print("New budget must be greater than 0.")
        
#Task 3:Add Budget Functionality

    budget = {}
    def add_expense():
        try:
            catname = input("Enter category of expense: ")
            catexpense = int(input("Enter budget for category: "))
            if self.get_allbudget >= catexpense and catexpense >= 0:
                new_allbudget = self.get_allbudget - catexpense
                budget[catname].set_allbudget(new_allbudget)
                budget.update({"expense": catexpense})

        except ValueError:
            print(f"{catexpense} must be greater than 0.")
    
    def display_category_summary(budget):
        print("Current budget expenses")
        print(f"Category {self.get_category}, Budget {self.get_allbudget}, Expenses {catexpense}")


b1 = BudgetCategory("food", 300)
b2 = BudgetCategory("clothes", 50)

b1.add_expense
display_category_summary()"""

class BudgetCategory:
    def __init__(self, catname, allbudget):
        self.__catname = catname
        self.__allbudget = allbudget
    # Getters
    def get_catname(self):
        return self.__catname
    def get_allbudget(self):
        return self.__allbudget
    # Setters
    def set_catname(self, new_catname):
        self.__catname = new_catname
    def set_allbudget(self, new_allbudget):
        if new_allbudget >= 0:
            self.__allbudget = new_allbudget
        else:
            print("New budget must be greater than or equal to 0.")
    # Add Expense
    def add_expense(get_catname, get_allbudget, catexpense):
        try:
            catname = input("Enter category of expense: ")
            catexpense = int(input("Enter budget for category: "))
            if self.get_allbudget() >= catexpense and catexpense >= 0:
                new_allbudget = self.get_allbudget() - catexpense
                self.set_allbudget(new_allbudget)
                if catname not in self.budget:
                    self.budget[catname] = 0
                self.budget[catname] += catexpense
            else:
                print("Expense exceeds budget or is negative.")
        except ValueError:
            print("Expense must be a positive integer.")
    # Display Summary
    budget = {}
    def display_category_summary(self):
        print("Current budget expenses:")
        for self.catname, self.allbudget in self.budget.items():
            print(f"Category: {self.catname}, Expense: {catexpense}")

b1 = BudgetCategory("food", 300)

#b1.add_expense(200)

b1.display_category_summary()

    

