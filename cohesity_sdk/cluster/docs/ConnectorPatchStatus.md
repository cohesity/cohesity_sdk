# ConnectorPatchStatus

Specifies patch status for the data-source connector. For example when the patch started, current status of the patch, errors for patch failure etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str, none_type** | Specifies error message for patch failure. Will be non empty if the patch failed. In all other cases, this will be empty. | [optional] 
**last_status_fetched_timestamp_msecs** | **int, none_type** | Specifies the most recent timestamp in UNIX time (milliseconds) when the connector patch status(InProgress/ Failed/Success/NotStarted) was fetched. | [optional] 
**start_timestamp_msecs** | **int, none_type** | Specifies the timestamp in UNIX time (milliseconds) when the connector patch was triggered. | [optional] 
**status** | **str** | Specifies the last fetched patch status of the connector. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


