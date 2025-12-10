# AzureTableStorageProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure Table Storage workload. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_table_storage_tag_ids** | **List[List[int]]** | Array of arrays of Table Storage Tag Ids that specify storage table to Exclude. | [optional] 
**objects** | [**List[AzureTableStorageProtectionGroupObjectParams]**](AzureTableStorageProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**table_storage_tag_ids** | **List[List[int]]** | Array of arrays of Table Storage Tag Ids that specify storage table to Protect. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_table_storage_protection_group_params import AzureTableStorageProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTableStorageProtectionGroupParams from a JSON string
azure_table_storage_protection_group_params_instance = AzureTableStorageProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureTableStorageProtectionGroupParams.to_json())

# convert the object into a dict
azure_table_storage_protection_group_params_dict = azure_table_storage_protection_group_params_instance.to_dict()
# create an instance of AzureTableStorageProtectionGroupParams from a dict
azure_table_storage_protection_group_params_from_dict = AzureTableStorageProtectionGroupParams.from_dict(azure_table_storage_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


