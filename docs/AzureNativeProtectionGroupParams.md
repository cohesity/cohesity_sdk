# AzureNativeProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups using Azure native snapshot APIs. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AzureNativeProtectionGroupObjectParams]**](AzureNativeProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**vm_tag_ids** | **[[int]], none_type** | Array of arrays of VM Tag Ids that Specify VMs to Protect. | [optional] 
**exclude_vm_tag_ids** | **[[int]], none_type** | Array of arrays of VM Tag Ids that Specify VMs to Exclude. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**cloud_migration** | **bool, none_type** | Specifies whether or not to move the workload to the cloud. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


