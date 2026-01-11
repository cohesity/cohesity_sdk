# ClusterNodeOperationStatus

Status of operation on a node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[OperationEvents]**](OperationEvents.md) | Specifies the list of events that took place during the operation.  | [optional] 
**id** | **int, none_type** | Specifies the ID of the node. | [optional] 
**ip** | **str, none_type** | Specifies the IP address of the node. | [optional] 
**percentage** | **int** | Specifies the approximate completion percentage for the operation. | [optional] 
**status** | **str, none_type** | Specifies the status of the operation. &#x60;Success&#x60; indicates the operation is successful. &#x60;Failed&#x60; indicates the operation failed due to an error. &#x60;InProgress&#x60; indicates the operation is in progress.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


