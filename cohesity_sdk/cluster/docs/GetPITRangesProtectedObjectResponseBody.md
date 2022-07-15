# GetPITRangesProtectedObjectResponseBody

Specifies the points in time available for restore as a set of one or more time ranges. If the number of available ranges exceeds 1000, then the latest 1000 will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_ranges** | [**[RecoveryTimeRangeInfo], none_type**](RecoveryTimeRangeInfo.md) | Specifies the time ranges within which this object can be restored to any point in time. If the number of available ranges exceeds 1000, then the latest 1000 will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


