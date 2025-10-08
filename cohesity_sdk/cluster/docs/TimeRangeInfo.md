# TimeRangeInfo

Information about a set of disjoint, possibly annotated time ranges.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str, none_type** | Error (if any) associated with the time range. | [optional] 
**time_ranges** | [**[RecoveryTimeRangeInfo], none_type**](RecoveryTimeRangeInfo.md) | The set of time ranges, each of which may be tagged with its job. These ranges will be non-overlapping and sorted by increasing start time. | [optional] 
**user_message** | **str, none_type** | User message (if any) associated with the time range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


