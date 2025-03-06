# KeyValuePair

Specifies a map structure to store Key and Values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key | 
**value** | **str** | value | 

## Example

```python
from cohesity_sdk.cluster.models.key_value_pair import KeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePair from a JSON string
key_value_pair_instance = KeyValuePair.from_json(json)
# print the JSON string representation of the object
print(KeyValuePair.to_json())

# convert the object into a dict
key_value_pair_dict = key_value_pair_instance.to_dict()
# create an instance of KeyValuePair from a dict
key_value_pair_from_dict = KeyValuePair.from_dict(key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


