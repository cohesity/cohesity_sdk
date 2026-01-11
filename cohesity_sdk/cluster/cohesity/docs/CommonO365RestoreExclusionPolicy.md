# CommonO365RestoreExclusionPolicy

Specifies the common filter policy to be applied for item exclusions in Microsoft 365 restore.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_after_time_secs** | **int, none_type** | Any items after this time will be excluded from restore. The time is specified as number of seconds after snapshot time. | [optional] 
**exclude_all** | **bool, none_type** | All items will be excluded from restore. | [optional] 
**exclude_before_time_secs** | **int, none_type** | Any items before this time will be excluded from restore. The time is specified as number of seconds before snapshot time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


