# Given a recipe and available ingredients.
# Find the max number of cakes you can make

def cakes(recipe, available):
    max_cakes = float('inf')
    # Iterate through each ingredient in the recipe and with amount for its value
    for ingredient, amount in recipe.items():
        # Check if ingredients are available
        if ingredient not in available:
            return 0
        # Calculate the maximum number of cakes that can be made based on the available quantity of the ingredient
        max_cakes = min(max_cakes, available[ingredient] // amount)
    return max_cakes


# Best Practise

def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)