# PureProtectionGroupObjectParams

Specifies the object parameters to create Pure Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.pure_protection_group_object_params import PureProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of PureProtectionGroupObjectParams from a JSON string
pure_protection_group_object_params_instance = PureProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(PureProtectionGroupObjectParams.to_json())

# convert the object into a dict
pure_protection_group_object_params_dict = pure_protection_group_object_params_instance.to_dict()
# create an instance of PureProtectionGroupObjectParams from a dict
pure_protection_group_object_params_from_dict = PureProtectionGroupObjectParams.from_dict(pure_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


