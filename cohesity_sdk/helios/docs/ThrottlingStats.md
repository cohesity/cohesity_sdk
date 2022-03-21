# ThrottlingStats

Specifies the timestamp and corresponding metric values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int, none_type** | Specifies the timestamp in milliseconds since the epoch when the stat was recorded. | [optional] 
**num_bytes_read** | **int, none_type** | Specifies the total bytes read from source. | [optional] 
**num_api_calls** | **int, none_type** | Specifies the total number of API calls made to source. | [optional] 
**idle_time** | **int, none_type** | Specifies the time spent idle due to throttling. | [optional] 
**total_response_time** | **int, none_type** | Specifies the time spent to complete API call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


