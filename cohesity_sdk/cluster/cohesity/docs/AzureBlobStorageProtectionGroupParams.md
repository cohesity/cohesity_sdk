# AzureBlobStorageProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure Blob Storage workload. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_storage_tag_ids** | **[[int]], none_type** | Array of arrays of Blob Storage Tag Ids that specify blob instances to Protect. | [optional] 
**exclude_blob_storage_tag_ids** | **[[int]], none_type** | Array of arrays of Blob Storage Tag Ids that specify blob instances to Exclude. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[AzureBlobStorageProtectionGroupObjectParams]**](AzureBlobStorageProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


