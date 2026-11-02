# Program 8: Store and manage product details using CRUD
# Example I/O:
#   Menu: 1.Add 2.View 3.Update price 4.Delete 5.Exit

products = {}       # product id -> {name, price}

while True:
    print("\n1. Add  2. View  3. Update price  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            pid = input("Product ID: ")
            products[pid] = {"name": input("Name: "), "price": float(input("Price: "))}
            print("Product added.")
        elif choice == "2":
            if not products:
                print("No products.")
            for pid, p in products.items():
                print(pid, p["name"], p["price"])
        elif choice == "3":
            pid = input("Product ID: ")
            if pid in products:
                products[pid]["price"] = float(input("New price: "))
                print("Price updated.")
            else:
                print("Product not found.")
        elif choice == "4":
            pid = input("Product ID: ")
            print("Deleted." if products.pop(pid, None) else "Product not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Price must be a number.")
