# ProtectionObjectInput

Specifies an object protected by a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.protection_object_input import ProtectionObjectInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionObjectInput from a JSON string
protection_object_input_instance = ProtectionObjectInput.from_json(json)
# print the JSON string representation of the object
print(ProtectionObjectInput.to_json())

# convert the object into a dict
protection_object_input_dict = protection_object_input_instance.to_dict()
# create an instance of ProtectionObjectInput from a dict
protection_object_input_from_dict = ProtectionObjectInput.from_dict(protection_object_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


