# AzureSnapshotManagerProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups using Azure native snapshot orchestration with snapshot manager. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_pre_post_script** | [**CloudBackupScriptParams**](CloudBackupScriptParams.md) |  | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_vm_tag_ids** | **List[List[int]]** | Array of arrays of VM Tag Ids that Specify VMs to Exclude. | [optional] 
**objects** | [**List[AzureSnapshotManagerProtectionGroupObjectParams]**](AzureSnapshotManagerProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**vm_tag_ids** | **List[List[int]]** | Array of arrays of VM Tag Ids that Specify VMs to Protect. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_snapshot_manager_protection_group_params import AzureSnapshotManagerProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSnapshotManagerProtectionGroupParams from a JSON string
azure_snapshot_manager_protection_group_params_instance = AzureSnapshotManagerProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureSnapshotManagerProtectionGroupParams.to_json())

# convert the object into a dict
azure_snapshot_manager_protection_group_params_dict = azure_snapshot_manager_protection_group_params_instance.to_dict()
# create an instance of AzureSnapshotManagerProtectionGroupParams from a dict
azure_snapshot_manager_protection_group_params_from_dict = AzureSnapshotManagerProtectionGroupParams.from_dict(azure_snapshot_manager_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


