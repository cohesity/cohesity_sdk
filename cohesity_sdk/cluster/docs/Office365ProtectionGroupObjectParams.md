# Office365ProtectionGroupObjectParams

Specifies the object parameters to create a Office 365 Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.office365_protection_group_object_params import Office365ProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ProtectionGroupObjectParams from a JSON string
office365_protection_group_object_params_instance = Office365ProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(Office365ProtectionGroupObjectParams.to_json())

# convert the object into a dict
office365_protection_group_object_params_dict = office365_protection_group_object_params_instance.to_dict()
# create an instance of Office365ProtectionGroupObjectParams from a dict
office365_protection_group_object_params_from_dict = Office365ProtectionGroupObjectParams.from_dict(office365_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


