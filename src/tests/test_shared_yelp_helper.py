

# test yelp search request builder
from ..core.shared.yelp.helper.apiAuthenticationSingleton import ApiAuthenticationSingleton
from ..core.shared.yelp.helper.yelpSearchRequestBuilder import YelpSearchRequestBuilder


# def test_try_credentials():
#     instance = ApiAuthenticationSingleton()
#     result = instance.try_credentials()

#     assert result == True


def test_add_param_new_key():
    builder = YelpSearchRequestBuilder()
    builder.add_param("key1", "value1")

    assert "key1" in builder._params
    assert builder._params["key1"] == "value1"


def test_add_param_update_key():
    builder = YelpSearchRequestBuilder()
    builder.add_param("key1", "value1")
    builder.add_param("key1", "new_value")

    assert builder._params["key1"] == "new_value"


def test_add_param_multiple_keys():
    builder = YelpSearchRequestBuilder()
    builder.add_param("key1", "value1")
    builder.add_param("key2", "value2")

    assert "key1" in builder._params and "key2" in builder._params
    assert builder._params["key1"] == "value1"
    assert builder._params["key2"] == "value2"
