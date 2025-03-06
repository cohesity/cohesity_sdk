# AzureTargetConfig

Specifies the configuration for adding Azure as replication target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the Azure Replication target. | [optional] [readonly] 
**resource_group** | **int** | Specifies id of the Azure resource group used to filter regions in UI. | [optional] 
**resource_group_name** | **str** | Specifies name of the Azure resource group used to filter regions in UI. | [optional] [readonly] 
**source_id** | **int** | Specifies the source id of the Azure protection source registered on Cohesity cluster. | 
**storage_account** | **int** | Specifies id of the storage account of Azure replication target which will contain storage container. | [optional] [readonly] 
**storage_account_name** | **str** | Specifies name of the storage account of Azure replication target which will contain storage container. | [optional] [readonly] 
**storage_container** | **int** | Specifies id of the storage container of Azure Replication target. | [optional] [readonly] 
**storage_container_name** | **str** | Specifies name of the storage container of Azure Replication target. | [optional] [readonly] 
**storage_resource_group** | **int** | Specifies id of the storage resource group of Azure Replication target. | [optional] [readonly] 
**storage_resource_group_name** | **str** | Specifies name of the storage resource group of Azure Replication target. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_config import AzureTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetConfig from a JSON string
azure_target_config_instance = AzureTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AzureTargetConfig.to_json())

# convert the object into a dict
azure_target_config_dict = azure_target_config_instance.to_dict()
# create an instance of AzureTargetConfig from a dict
azure_target_config_from_dict = AzureTargetConfig.from_dict(azure_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


