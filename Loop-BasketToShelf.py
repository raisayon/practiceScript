# Ask the user for the number of items in each basket
# Example input: "3 5 2" (space-separated) or "3,5,2" (comma-separated)
user_input = input("Enter the number of items in each basket (separated by spaces or commas): ")

# Clean up and convert to a list of integers
# Replace commas with spaces, then split on whitespace
input_clean = user_input.replace(",", " ")
basket_sizes = [int(x) for x in input_clean.split() if x.strip().isdigit()]

# If the user entered nothing, provide a default
if not basket_sizes:
    print("No valid numbers entered. Using default [1,2,3,4]")
    basket_sizes = [1, 2, 3, 4]

# Now process each basket
for idx, total_items in enumerate(basket_sizes, start=1):
    print(f"\nBasket {idx} has {total_items} items.")
    remaining = total_items
    shelf_counter = 1
    
    while remaining > 0:
        print(f"  Putting item {shelf_counter} on shelf ...")
        remaining -= 1          # deduct one item
        shelf_counter += 1
    
    print(f"Basket {idx} now has {remaining} items (all placed).")
