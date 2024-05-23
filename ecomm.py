#E-commerce Product Catalog System
#Task 1:Create Base Product Class

class Product:
    def __init__(self, productID, name, price):
        self.productID = productID
        self.name = name
        self.price = price

def display_product(productID, name, price):
    print("***Store Items***")
    print(f"{productID}, {name}, {price}")

b1 = Product("256143", "Ginger Ale", 15.42)
display_product("256143", "Ginger Ale", 15.42)

#Task 2:Implement Subclasses for Specific Products
#Task 3:Override Display Method in Subclasses
#Task 4:Test Product Catalog Functionality
#Last 3 tasks are combined together.

class Book(Product):
    def __init__(self, productID, name, price, author, genre):
        super().__init__(productID, name, price)
        self.author = author
        self.genre = genre

    #Override display for Book class
    def display_product(productID, name, price):
        print("***Store Book Items***")
        print(f"{productID}, {name}, {price}, {author}, {genre}")

class Electronic(Product):
    def __init__(self, productID, name, price, monitors, gaming):
        super().__init__(productID, name, price)
        self.monitors = monitors
        self.gaming = gaming

    #Override display for Electronic class
    def display_product(productID, name, price):
        print("***Store Electronic Items***")
        print(f"{productID}, {name}, {price}, {monitors}, {gaming}")

class Clothing(Product):
    def __init__(self, productID, name, price, kids, women, mens):
        super().__init__(productID, name, price)
        self.kids = kids
        self.women = women
        self.men = mens

    #Override display for Clothing class
    def display_product(productID, name, price):
        print("***Store Clothing Items***")
        print(f"{productID}, {name}, {price}, {kids}, {women}, {mens}")

b2 = Book("1369", "The Hidden Stairs", 18.00, "Johnny Myles", "mystery")
#b2.display_product("1369", "The Hidden Stairs", 18.00, "Johnny Myles", "mystery")
print(f"The genre, written by {b2.author}, is a {b2.genre}.")




