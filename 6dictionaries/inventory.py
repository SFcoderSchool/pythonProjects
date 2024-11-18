# Inventory Management System
# Description: Simulate an inventory system where products are stored as dictionary keys and quantities as values. Allow adding, removing, and updating inventory items, and generating reports for low stock.
# Dictionary Use: Store product names as keys and quantities as values.

inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20,
    "Milk": 15,
    "Bread": 25,
    "Eggs": 40,
    "Cheese": 10,
    "Chicken": 8,
    "Rice": 100,
    "Pasta": 60
}

def update_inventory(inventory, updates):
    for product, change in updates.items():
        if product in inventory:
            inventory[product] += change
        else:
            inventory[product] = change  # Adds a new product if not already in inventory

# Example usage
updates = {
    "Apples": -5,
    "Oranges": 10,
    "Bread": -2,
    "New Product": 20  # Adds a new product to the inventory
}

update_inventory(inventory, updates)