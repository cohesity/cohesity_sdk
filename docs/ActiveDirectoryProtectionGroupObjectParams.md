# ActiveDirectoryProtectionGroupObjectParams

Specifies the object identifier to for the active directory protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_params** | [**List[ActiveDirectoryAppParams]**](ActiveDirectoryAppParams.md) | Specifies the specific parameters required for active directory app configuration. | [optional] 
**enable_system_backup** | **bool** | Specifies whether to take bmr backup. If this is not specified, the bmr backup won&#39;t be enabled. | [optional] 
**source_id** | **int** | Specifies the id of the registered active directory source. | 
**source_name** | **str** | Specifies the name of the registered active directory source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.active_directory_protection_group_object_params import ActiveDirectoryProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryProtectionGroupObjectParams from a JSON string
active_directory_protection_group_object_params_instance = ActiveDirectoryProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryProtectionGroupObjectParams.to_json())

# convert the object into a dict
active_directory_protection_group_object_params_dict = active_directory_protection_group_object_params_instance.to_dict()
# create an instance of ActiveDirectoryProtectionGroupObjectParams from a dict
active_directory_protection_group_object_params_from_dict = ActiveDirectoryProtectionGroupObjectParams.from_dict(active_directory_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


