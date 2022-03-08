# GetPITRangesProtectedObjectResponseBody

Specifies the points in time available for restore as a set of one or more time ranges. If the number of available ranges exceeds 1000, then the latest 1000 will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment for which restore ranges are returned. | [optional]  if omitted the server will use the default value of "kOracle"
**oracle_restore_range_info** | [**OracleRestoreRangeInfo**](OracleRestoreRangeInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


