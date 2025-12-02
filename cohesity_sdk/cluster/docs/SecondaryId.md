# SecondaryId

Specifies the secondary ID for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies name of the secondary ID for an object. | 
**value** | **str** | Specifies value of the secondary ID for an object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.secondary_id import SecondaryId

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryId from a JSON string
secondary_id_instance = SecondaryId.from_json(json)
# print the JSON string representation of the object
print(SecondaryId.to_json())

# convert the object into a dict
secondary_id_dict = secondary_id_instance.to_dict()
# create an instance of SecondaryId from a dict
secondary_id_from_dict = SecondaryId.from_dict(secondary_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


