# TheMealDb Documentation

## Basic Usage

1. Instantiate TheMealDb

```Python
the_meal_db = TheMealDb()
```

2. Call the method you want

```Python
json_data = the_meal_db.search_meal_by_name("Arrabiata")
```

3. Utilize the `json_data` object

```Python
json_data["meals"]
```

Note: Not all methods respond with an array or the `meals` object.

## Methods

The following methods are available:

- `search_meal_by_name`: Search a meal by name

  - Parameters: `name` (e.g., "Arrabiata")
  - Returns: `{ meals: [objects]}`

  Full return example:

  ```
  {'meals': [{'idMeal': '52771', 'strMeal': 'Spicy Arrabiata Penne', ...}]}

  # Include other method details similarly
  ```

- `list_all_meals_by_first_letter`: Search a meal by the first letter

  - Parameters: `name` (e.g., "a")
  - Returns: `{ meals: [objects]}`

- `lookup_meal_details_by_id`: Search a meal by ID

  - Parameters: `id` (e.g., 52772)
  - Returns: `{ meals: [objects]}`

- `lookup_single_random_meal`: Find a single random meal

  - Parameters: None
  - Returns: `{ meals: [objects]}`

- `lookup_categories`: Lookup all categories

  - Parameters: None
  - Returns: `{ categories: [objects]}`

  Full return example:

  ```
  {'categories': [{'idCategory': '1', 'strCategory': 'Beef', ...}]}

  # Include other categories similarly
  ```
