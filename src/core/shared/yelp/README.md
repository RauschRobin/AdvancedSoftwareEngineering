# Yelp Documentation

This module provides a Python class, Yelp, to interact with the Yelp API for retrieving restaurant data based on location, radius, and categories.

## Basic Usage

1. Create a new instance of Yelp:

```Python
yelp = Yelp()
```

2. Call the method you want, for example:

```Python
json_data = yelp.get_restaurants_by_location_limit_radius_categories("NYC", 5, 1000, "bars,french")
```

3. Utilize the `json_data` object, accessing elements like:

```Python
json_data["businesses"][0]
```

## Class Methods

### `get_restaurants_by_location_limit`

Returns a list of restaurants near the specified location within a limit.

**Parameters:**

- `location` (string): Location identifier (e.g., "New York City", "NYC")
- `limit` (int): Limit on the number of results to retrieve

**Returns:**

- JSON object with businesses data

### `get_restaurants_by_location_limit_radius`

Returns a list of restaurants near the specified location within a given radius.

**Parameters:**

- `location` (string): Location identifier (e.g., "New York City", "NYC")
- `limit` (int): Limit on the number of results to retrieve
- `radius` (int): Radius in meters (max 40,000)

**Returns:**

- JSON object with businesses data

### `get_restaurants_by_location_limit_radius_categories`

Returns a list of restaurants near the specified location within a given radius and matching specified categories.

**Parameters:**

- `location` (string): Location identifier (e.g., "New York City", "NYC")
- `limit` (int): Limit on the number of results to retrieve
- `radius` (int): Radius in meters (max 40,000)
- `categories` (string): Comma-delimited categories (e.g., "bars,french")

**Returns:**

- JSON object with businesses data

### `get_restaurants_by_location_limit_radius_categories_price`

Returns a list of restaurants near the specified location within a given radius, matching specified categories and price.

**Parameters:**

- `location` (string): Location identifier (e.g., "New York City", "NYC")
- `limit` (int): Limit on the number of results to retrieve
- `radius` (int): Radius in meters (max 40,000)
- `categories` (string): Comma-delimited categories (e.g., "bars,french")
- `price` (int): Price range (1 = $, 2 = $$, 3 = $$$, 4 = $$$$)

**Returns:**

- JSON object with businesses data
