# AzureSnapshotManagerProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups using Azure native snapshot orchestration with snapshot manager. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AzureSnapshotManagerProtectionGroupObjectParams]**](AzureSnapshotManagerProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**vm_tag_ids** | **[[int]], none_type** | Array of arrays of VM Tag Ids that Specify VMs to Protect. | [optional] 
**exclude_vm_tag_ids** | **[[int]], none_type** | Array of arrays of VM Tag Ids that Specify VMs to Exclude. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


