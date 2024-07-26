# Disk

Specifies the details of a disk that belongs to a node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_bytes** | **int, none_type** | Specifies capacity of disk in bytes. | [optional] 
**encryption_status** | **str** | Specifies disk encryption state. | [optional] 
**id** | **int, none_type** | Specifies id to uniquely identify a disk. | [optional] 
**location** | **str, none_type** | Specifies location of the disk in node. | [optional] 
**model** | **str, none_type** | Specifies product model of disk. | [optional] 
**node_id** | **int, none_type** | Specifies node id of the node that this disk belong to. | [optional] 
**precheck_timestamp_secs** | **int, none_type** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**progress_percentage** | **int, none_type** | Specifies the overall progress percentage in removing the Disk. | [optional] 
**removal_progress_list** | [**[ComponentRemovalProgress], none_type**](ComponentRemovalProgress.md) | Specifies the removal progress details for services that are not acked yet. | [optional] 
**removal_reason** | **str, none_type** | Specifies the removal reason of the disk. | [optional] 
**removal_timestamp_secs** | **int, none_type** | Specifies the Unix epoch timestamp (in seconds) when the Disk was marked for removal. | [optional] 
**serial_number** | **str, none_type** | Specifies serial number of disk. | [optional] 
**services_acked_list** | **[str], none_type** | Specifies the services already ACKed for removal of this entity. | [optional] 
**services_not_acked** | **str, none_type** | Specifies the services that are not ACKed after disk is marked for removal. | [optional] 
**services_not_acked_list** | **[str], none_type** | Specifies the services not ACKed yet for removal of this entity. | [optional] 
**ssd_used_percentage** | **int, none_type** | Specifies SSD used percentage. | [optional] 
**status** | **str** | Specifies status of the disk. | [optional] 
**time_remaining** | **int, none_type** | Specifies the total duration in seconds left to remove the Disk. | [optional] 
**type** | **str** | Specifies type of the disk. | [optional] 
**validation_checks** | [**[PreCheckValidation], none_type**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


