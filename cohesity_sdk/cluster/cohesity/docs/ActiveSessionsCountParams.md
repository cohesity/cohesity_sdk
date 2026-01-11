# ActiveSessionsCountParams

Specifies the number of sessions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions_per_user** | [**[UserSessionsCount]**](UserSessionsCount.md) | Specifies the sessions count per user. | [optional] 
**total_sessions_count** | **int** | Specifies the aggregated sessions count for the user sessions returned. If sids are not given this returns the total system wide sessions count and if the sids are given, this returns the total sessions count for the given sids. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


