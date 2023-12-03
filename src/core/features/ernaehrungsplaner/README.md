# Ernaehrungsplaner

This module implements a meal planner, providing suggestions for lunch and dinner, including details about restaurants, meals to cook, and shopping lists. It utilizes various helper modules and external APIs to enhance the user's meal planning experience.

## Usage

### Initialize Ernaehrungsplaner Object

```python
from ernaehrungsplaner_module import Ernaehrungsplaner

ernaehrungsplaner = Ernaehrungsplaner(voice_output)
```

### Suggest Restaurant for Lunchbreak

```python
# Suggest a restaurant for lunchbreak
ernaehrungsplaner.suggest_restaurant_for_lunchbreak()
```

### Tell Dinner Meal and Missing Ingredients

```python
# Get details about the dinner meal and missing ingredients
ernaehrungsplaner.tell_dinner_meal_and_missing_ingredients()
```

### How to Cook the Meal

```python
# Provide instructions on how to cook the specified meal
ernaehrungsplaner.how_to_cook_the_meal()
```

### Cook Something Different

```python
# Find and suggest a random meal to cook
ernaehrungsplaner.cook_something_different()
```

### Ingredients at Home to Cook

```python
# Get a list of ingredients at home for the specified or random meal
ernaehrungsplaner.ingredients_at_home_to_cook()
```

### Generate Shopping List for Meal

```python
# Generate a shopping list for the specified or random meal
ernaehrungsplaner.generate_shopping_list_for_meal()
```

## API Reference

### `__init__(voice_output: VoiceOutput)`

Initializes the Ernaehrungsplaner class with a VoiceOutput instance.

### `run()`

Starts the while loop of the Ernaehrungsplaner feature.

### `start_ernaehrungsplaner_loop()`

Runs the while loop of the Ernaehrungsplaner feature.

### `suggest_restaurant_for_lunchbreak()`

Proactively suggests restaurant options for lunchbreak.

### `tell_dinner_meal_and_missing_ingredients()`

Proactively provides information about the dinner meal and missing ingredients.

### `how_to_cook_the_meal()`

Enables the user to get detailed meal information and cooking instructions.

### `cook_something_different()`

Finds and suggests a random meal to cook.

### `ingredients_at_home_to_cook()`

Provides a list of ingredients at home for the specified or random meal.

### `generate_shopping_list_for_meal()`

Generates a shopping list for the specified or random meal.

Feel free to customize this README with additional details or examples to suit your users' needs!
