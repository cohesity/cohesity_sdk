# UdaSearchParams

Specifies the parameters which are specific for searching Universal Data Adapter objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str** | Specifies the search string to search the Universal Data Adapter Objects | 

## Example

```python
from cohesity_sdk.helios.models.uda_search_params import UdaSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaSearchParams from a JSON string
uda_search_params_instance = UdaSearchParams.from_json(json)
# print the JSON string representation of the object
print(UdaSearchParams.to_json())

# convert the object into a dict
uda_search_params_dict = uda_search_params_instance.to_dict()
# create an instance of UdaSearchParams from a dict
uda_search_params_from_dict = UdaSearchParams.from_dict(uda_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


