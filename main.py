import pyfiglet


sales_items = [
    {
        "id": "001",
        "name": "Smartphone",
        "category": "Electronics",
        "price": 699.99,
        "stock": 25,
        "features": {
            "brand": "TechBrand",
            "model": "X10 Pro",
            "screenSize": "6.5 inches",
            "color": "Midnight Black"
        }
    },
    {
        "id": "002",
        "name": "Laptop",
        "category": "Electronics",
        "price": 1299.99,
        "stock": 15,
        "features": {
            "brand": "ComputeCo",
            "model": "UltraBook 2024",
            "processor": "Intel i7",
            "ram": "16GB",
            "storage": "512GB SSD"
        }
    },
    {
        "id": "003",
        "name": "Bluetooth Headphones",
        "category": "Accessories",
        "price": 149.99,
        "stock": 50,
        "features": {
            "brand": "SoundWave",
            "model": "HP-5000",
            "batteryLife": "20 hours",
            "color": "Silver"
        }
    },
    {
        "id": "004",
        "name": "Coffee Maker",
        "category": "Home Appliances",
        "price": 89.99,
        "stock": 30,
        "features": {
            "brand": "BrewMaster",
            "model": "CM-2024",
            "capacity": "12 cups",
            "color": "Red"
        }
    },
    {
        "id": "005",
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 99.99,
        "stock": 40,
        "features": {
            "brand": "StridePro",
            "model": "RS-150",
            "size": "Various",
            "color": "Blue"
        }
    }
]

# Example of accessing a specific item's details
#for item in sales_items:
#    print(f"Item Name: {item['name']}")
#    print(f"Price: ${item['price']:.2f}")
#    print(f"Stock: {item['stock']}")
#    print("Features:")
#    for key, value in item['features'].items():
#        print(f"  {key}: {value}")
#    print()


def main():
    title = pyfiglet.figlet_format("Welcome to E-Comm", font = "slant")
    print(title)
    while True:
        print("---------------------------------------------")
        print("1: View All Items")
        print("   - Caution: Will Have To View Every Single Item On Record")
        print("2: Search For Specific Item")
        print("   - Views Only 1 Item")
        print("3: Browse By Category")
        print("   - Don't Recall the name of a product? Search by Category to")
        print("     Narrow the Results Down")
        print("4: Exit\n")
        choice = input("Enter the number tied to the option you want\n")
        print("\n")

        if (choice == '1'):
            print("Would you also like to see the features of each item?")
            option = input("Enter y or n\n")

            for item in sales_items:
                print(f"Item Name: {item['name']}")
                print(f"Price: ${item['price']:.2f}")
                if(option == "y"):
                    print("Features:")
                    for key, value in item['features'].items():
                        print(f"  {key}: {value}")
                print("\n")

        elif (choice == '2'):
            found = False
            product = input("What item are you looking for?\n")
            print("\n")
            print("Would you also like to see the features of the item?")
            option = input("Enter y or n\n")

            for item in sales_items:
                if(item['name'] == product):
                    print(f"Item Name: {item['name']}")
                    print(f"Price: ${item['price']:.2f}")
                    print(f"Stock: {item['stock']}")
                    if(option == "y"):
                        print("Features:")
                        for key, value in item['features'].items():
                            print(f"  {key}: {value}")
                    print("\n")

                    found = True
                    break
            
            if (found == False):
                print("Item was not found.")

        elif(choice == '3'):
            print("Which Catergory Would You Like To Search For?")
            print("1: Electronics")
            print("2: Accessories")
            print("3: Home Appliances")
            print("4: Footwear")
            print("5: Back To Home Page")
            cat = input("Type the number tied to the category you are interested in\n")
            categories = {
                "1": "Electronics",
                "2": "Accessories",
                "3": "Home Appliances",
                "4": "Footwear",
                "5": "Exit"
            }
            print("Would you also like to see the features of the item?")
            option = input("Enter y or n\n")

            for item in sales_items:
                if(item['category'] == categories[cat]):
                    print(f"Item Name: {item['name']}")
                    print(f"Price: ${item['price']:.2f}")
                    print(f"Stock: {item['stock']}")
                    if(option == "y"):
                        print("Features:")
                        for key, value in item['features'].items():
                            print(f"  {key}: {value}")
                    print("\n")


        elif (choice == '4'):
            break
        else:
            print("Input given is invalid, try again.\n")



if __name__ == "__main__":
    main()




