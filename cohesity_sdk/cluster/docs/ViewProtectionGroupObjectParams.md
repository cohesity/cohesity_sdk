# ViewProtectionGroupObjectParams

Specifies an object protected by a View Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.view_protection_group_object_params import ViewProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtectionGroupObjectParams from a JSON string
view_protection_group_object_params_instance = ViewProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(ViewProtectionGroupObjectParams.to_json())

# convert the object into a dict
view_protection_group_object_params_dict = view_protection_group_object_params_instance.to_dict()
# create an instance of ViewProtectionGroupObjectParams from a dict
view_protection_group_object_params_from_dict = ViewProtectionGroupObjectParams.from_dict(view_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


