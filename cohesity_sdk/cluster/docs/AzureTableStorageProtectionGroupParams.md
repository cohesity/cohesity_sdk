# AzureTableStorageProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure Table Storage workload. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_table_storage_tag_ids** | **[[int]], none_type** | Array of arrays of Table Storage Tag Ids that specify storage table to Exclude. | [optional] 
**objects** | [**[AzureTableStorageProtectionGroupObjectParams]**](AzureTableStorageProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**table_storage_tag_ids** | **[[int]], none_type** | Array of arrays of Table Storage Tag Ids that specify storage table to Protect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


