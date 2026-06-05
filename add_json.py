# This file is to Update JSON file catalog
import json
import os

FILENAME = "catalog.json"

def load_catalog():
    """Loads the catalog from the JSON file, or creates a default structure if it doesn't exist."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: {FILENAME} was corrupted. Starting with a fresh catalog.")
    
    # Default structure if file doesn't exist or is empty
    return {"products": []}

def save_catalog(data):
    """Saves the updated catalog dictionary back to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Catalog updated successfully!")

def get_user_input():
    """Prompts the user for product details with basic validation."""
    print("\n--- Add New Product ---")
    name = input("Enter product name: ").strip()
    
    # Get and validate price
    while True:
        try:
            price = float(input("Enter product price (e.g., 3.49): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")
            
    # Get and validate stock status
    while True:
        in_stock_input = input("Is it in stock? (yes/no): ").strip().lower()
        if in_stock_input in ['yes', 'y']:
            in_stock = True
            break
        elif in_stock_input in ['no', 'n']:
            in_stock = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
    return {
        "name": name,
        "price": price,
        "in_stock": in_stock
    }

def main():
    # 1. Load the existing JSON data
    catalog = load_catalog()
    
    # 2. Get the new product details from the user
    new_product = get_user_input()
    
    # 3. Append the new product to the 'products' list
    catalog["products"].append(new_product)
    
    # 4. Save the updated dictionary back to the file
    save_catalog(catalog)

if __name__ == "__main__":
    main()