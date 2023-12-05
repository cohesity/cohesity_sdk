# ClusterNodeOperationStatus

Specifies the operation status of the nodes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[OperationEvents]**](OperationEvents.md) | Specifies the list of events that took place during the operation. | [optional] 
**id** | **int, none_type** | Specifies the id of the node. | [optional] 
**ip** | **str, none_type** | Specifies the Ip address of the node. | [optional] 
**percentage** | **int** | Specifies an approximate completion percentage for the operation. | [optional] 
**status** | **str, none_type** | Specifies the status of the operation. &#39;Success&#39; indicates the operation is successful. &#39;Failed&#39; indicates the operation failed due to an error. &#39;InProgress&#39; indicates the operation is in progress. | [optional] 
**time_remaining_seconds** | **int** | Specifies an estimated number of seconds until the operation is complete. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


