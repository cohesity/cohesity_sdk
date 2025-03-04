# SearchExchangeObjectsRequestParams

Specifies the parameters which are specific for searching Exchange mailboxes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str** | Specifies the search string to search the Exchange Objects | 

## Example

```python
from cohesity_sdk.models.search_exchange_objects_request_params import SearchExchangeObjectsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExchangeObjectsRequestParams from a JSON string
search_exchange_objects_request_params_instance = SearchExchangeObjectsRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchExchangeObjectsRequestParams.to_json())

# convert the object into a dict
search_exchange_objects_request_params_dict = search_exchange_objects_request_params_instance.to_dict()
# create an instance of SearchExchangeObjectsRequestParams from a dict
search_exchange_objects_request_params_from_dict = SearchExchangeObjectsRequestParams.from_dict(search_exchange_objects_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


