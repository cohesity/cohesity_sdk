# NodeUnitProgress

Specifies the progress of the patch operation on a node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ip** | **str, none_type** | Specifies the IP address of the node. | [optional] 
**in_progress** | **bool, none_type** | Specifies whether a operation is in progress on the node. | [optional] 
**patch_level_transition** | **str, none_type** | Specifies the patch level transition of the patch operation. For Apply operation, patch level goes up for each operation. For Revert operation, patch level goes down. Patch level zero is the base level where no patch was applied. | [optional] 
**percentage** | **int, none_type** | Specifies the percentage of completion of the patch operation on the node. | [optional] 
**time_taken_seconds** | **int, none_type** | Specifies the time taken so far in this patch unit operation on the node. | [optional] 
**node_message** | **str, none_type** | Specifies a message about the patch operation on the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


