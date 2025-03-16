# AzureSnapshotManagerProtectionGroupObjectParams

Specifies the object parameters to create Azure Snapshot Manager Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.azure_snapshot_manager_protection_group_object_params import AzureSnapshotManagerProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSnapshotManagerProtectionGroupObjectParams from a JSON string
azure_snapshot_manager_protection_group_object_params_instance = AzureSnapshotManagerProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureSnapshotManagerProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_snapshot_manager_protection_group_object_params_dict = azure_snapshot_manager_protection_group_object_params_instance.to_dict()
# create an instance of AzureSnapshotManagerProtectionGroupObjectParams from a dict
azure_snapshot_manager_protection_group_object_params_from_dict = AzureSnapshotManagerProtectionGroupObjectParams.from_dict(azure_snapshot_manager_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


