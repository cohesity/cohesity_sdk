# Failover

Specifies the details of a failover.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int, none_type** | Specifies the failover complete time in micro seconds. | [optional] 
**error_message** | **str, none_type** | Specifies the error details if failover status is &#39;Failed&#39;. | [optional] 
**id** | **str, none_type** | Specifies the failover id. | [optional] 
**replications** | [**[FailoverReplication], none_type**](FailoverReplication.md) | Specifies a list of replications in this failover. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the failover start time in micro seconds. | [optional] 
**status** | **str, none_type** | Specifies the failover status. | [optional] 
**type** | **str, none_type** | Specifies the failover type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


