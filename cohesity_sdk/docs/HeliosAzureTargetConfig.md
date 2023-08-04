# HeliosAzureTargetConfig

Specifies the configuration for adding Azure as replication target

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int, none_type** | Specifies the source id of the Azure protection source registered on Cohesity cluster. | 
**name** | **str, none_type** | Specifies the name of the Azure Replication target. | [optional] [readonly] 
**resource_group** | **int, none_type** | Specifies id of the Azure resource group used to filter regions in UI. | [optional] 
**resource_group_name** | **str, none_type** | Specifies name of the Azure resource group used to filter regions in UI. | [optional] [readonly] 
**storage_account** | **int, none_type** | Specifies id of the storage account of Azure replication target which will contain storage container. | [optional] [readonly] 
**storage_account_name** | **str, none_type** | Specifies name of the storage account of Azure replication target which will contain storage container. | [optional] [readonly] 
**storage_container** | **int, none_type** | Specifies id of the storage container of Azure Replication target. | [optional] [readonly] 
**storage_container_name** | **str, none_type** | Specifies name of the storage container of Azure Replication target. | [optional] [readonly] 
**storage_resource_group** | **int, none_type** | Specifies id of the storage resource group of Azure Replication target. | [optional] [readonly] 
**storage_resource_group_name** | **str, none_type** | Specifies name of the storage resource group of Azure Replication target. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


