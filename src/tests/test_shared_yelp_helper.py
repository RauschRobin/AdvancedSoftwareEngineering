

# test yelp search request builder
from ..core.shared.yelp.helper.yelpSearchRequestBuilder import YelpSearchRequestBuilder


def test_add_param_new_key():
    builder = YelpSearchRequestBuilder()
    builder.add_param("key1", "value1")

    assert "key1" in builder._params
    assert builder._params["key1"] == "value1"
