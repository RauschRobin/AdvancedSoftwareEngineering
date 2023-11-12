# Yelp Documentation

## Basic Usage

1. Create a new instance of Yelp

```Python
yelp = Yelp()
```

2. Call the method you want

```Python
json_data = yelp.get_restaurants_by_location_limit_radius_categories("NYC", 1, 1000, "bars,french")
```

3. Use the json_data object (get the first index of the array)

```Python
json_data["businesses"][0]
```

## Methods

The following methods are available:

- get_restaurants_by_location_limit
- get_restaurants_by_location_limit_radius
- get_restaurants_by_location_limit_radius_categories

### get_restaurants_by_location_limit

Returns a list of restaurants near that location with a given radius and categories (return limited)

Parameters: location e.g. "New York City", "NYC"; limit: 5  
Returns: { "businesses": [{ obejct}]}

Full return example:

{'businesses': [{'id': 'veq1Bl1DW3UWMekZJUsG1Q', 'alias': 'gramercy-tavern-new-york', 'name': 'Gramercy Tavern', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/l2oSnhyvJfWT6bufumBMzw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/gramercy-tavern-new-york?adjust_creative=0IdQKG7ucDLgDb9QYe7q3g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0IdQKG7ucDLgDb9QYe7q3g', 'review_count': 3405, 'categories': [{'alias': 'newamerican', 'title': 'New American'}], 'rating': 4.5, 'coordinates': {'latitude': 40.73844, 'longitude': -73.98825}, 'transactions': ['delivery'], 'price': '$$$$', 'location': {'address1': '42 E 20th St', 'address2': '', 'address3': '', 'city': 'New York', 'zip_code': '10003', 'country': 'US', 'state': 'NY', 'display_address': ['42 E 20th St', 'New York, NY 10003']}, 'phone': '+12124770777', 'display_phone': '(212) 477-0777', 'distance': 3695.6399277648}], 'total': 15000, 'region': {'center': {'longitude': -73.99429321289062, 'latitude': 40.70544486444615}}}

### get_restaurants_by_location_limit_radius

Returns a list of restaurants near that location with a given radius (return limited)

Parameters: location e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m)  
Returns: { "businesses": [{ obejct}]}

Full return example:

{'businesses': [{'id': 'ysqgdbSrezXgVwER2kQWKA', 'alias': 'julianas-brooklyn-3', 'name': "Juliana's", 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/od36nFW220aMFAnNP00ocw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/julianas-brooklyn-3?adjust_creative=0IdQKG7ucDLgDb9QYe7q3g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0IdQKG7ucDLgDb9QYe7q3g', 'review_count': 2708, 'categories': [{'alias': 'pizza', 'title': 'Pizza'}], 'rating': 4.5, 'coordinates': {'latitude': 40.70274718768062, 'longitude': -73.99343490196397}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '19 Old Fulton St', 'address2': '', 'address3': '', 'city': 'Brooklyn', 'zip_code': '11201', 'country': 'US', 'state': 'NY', 'display_address': ['19 Old Fulton St', 'Brooklyn, NY 11201']}, 'phone': '+17185966700', 'display_phone': '(718) 596-6700', 'distance': 308.56984360837544}], 'total': 409, 'region': {'center': {'longitude': -73.99429321289062, 'latitude': 40.70544486444615}}}

### get_restaurants_by_location_limit_radius_categories

Returns a list of restaurants near that location with a given radius and categories (return limited)

Parameters:blocation e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m); categories: Comma delimited e.g. "bars,french"
Returns: { "businesses": [{ obejct}]}

Full retrun example:
{'businesses': [{'id': '4XX-zF8h5Lvrr22_tqU6-Q', 'alias': 'the-river-café-brooklyn-3', 'name': 'The River Café', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/yPvMZQFBDMUN77vbkSag6w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-river-caf%C3%A9-brooklyn-3?adjust_creative=0IdQKG7ucDLgDb9QYe7q3g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0IdQKG7ucDLgDb9QYe7q3g', 'review_count': 1293, 'categories': [{'alias': 'newamerican', 'title': 'New American'}, {'alias': 'wine_bars', 'title': 'Wine Bars'}, {'alias': 'venues', 'title': 'Venues & Event Spaces'}], 'rating': 4.0, 'coordinates': {'latitude': 40.703866713051106, 'longitude': -73.99479360219303}, 'transactions': [], 'price': '$$$$', 'location': {'address1': '1 Water St', 'address2': '', 'address3': '', 'city': 'Brooklyn', 'zip_code': '11201', 'country': 'US', 'state': 'NY', 'display_address': ['1 Water St', 'Brooklyn, NY 11201']}, 'phone': '+17185225200', 'display_phone': '(718) 522-5200', 'distance': 180.48041752975385}], 'total': 61, 'region': {'center': {'longitude': -73.99429321289062, 'latitude': 40.70544486444615}}}

### get_restaurants_by_location_limit_radius_categories_price

Returns a list of restaurants near that location with a given radius, categories and price (return limited)

Parameters: location e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m); categories: Comma delimited e.g. "bars,french", price: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$ (cheap to expensive)
Returns: { "businesses": [{ obejct}]}

Full return example:

{'businesses': [{'id': 'bvba7OYmEvcO8kOEez35gw', 'alias': '169-bar-new-york-4', 'name': '169 Bar', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/2Ms4f7JPTY0PqPjkqLi8_w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/169-bar-new-york-4?adjust_creative=0IdQKG7ucDLgDb9QYe7q3g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0IdQKG7ucDLgDb9QYe7q3g', 'review_count': 498, 'categories': [{'alias': 'tradamerican', 'title': 'American'}, {'alias': 'divebars', 'title': 'Dive Bars'}], 'rating': 3.5, 'coordinates': {'latitude': 40.713838, 'longitude': -73.98976}, 'transactions': ['delivery'], 'price': '$', 'location': {'address1': '169 E Broadway', 'address2': None, 'address3': '', 'city': 'New York', 'zip_code': '10002', 'country': 'US', 'state': 'NY', 'display_address': ['169 E Broadway', 'New York, NY 10002']}, 'phone': '+15169867938', 'display_phone': '(516) 986-7938', 'distance': 1008.4626419883092}], 'total': 6, 'region': {'center': {'longitude': -73.99429321289062, 'latitude': 40.70544486444615}}}
