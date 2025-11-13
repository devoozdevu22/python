fruits =["Apple", "Banana", "Cherry"] 
Vegetables =["Carrot", "Tomato", "Spinach"]
Beverages =["Water", "Juice", "Soda"]
fruits.append("Orange")
Vegetables.insert(1, "Cucumber")
Beverages.pop()
inventory = [fruits, Vegetables, Beverages]
print("First two fruits:", fruits[:2])
print("Last vegetable:", Vegetables[-1])
fruits_lengths = [len(fruit) for fruit in fruits]
print("lengths of each fruit names:", fruits_lengths)
print("Is 'Water' in Beverages?", "Water" in Beverages)
first_item=(fruits[0],Vegetables[0],Beverages[0])
print("Tuple of first items from each section:", first_item)