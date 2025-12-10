# AzureTableStorageProtectionGroupObjectParams

Specifies the object parameters to create Azure Table Storage Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the azure source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_table_storage_protection_group_object_params import AzureTableStorageProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTableStorageProtectionGroupObjectParams from a JSON string
azure_table_storage_protection_group_object_params_instance = AzureTableStorageProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureTableStorageProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_table_storage_protection_group_object_params_dict = azure_table_storage_protection_group_object_params_instance.to_dict()
# create an instance of AzureTableStorageProtectionGroupObjectParams from a dict
azure_table_storage_protection_group_object_params_from_dict = AzureTableStorageProtectionGroupObjectParams.from_dict(azure_table_storage_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


