# UserQuotaSummaryForView

Specifies summary for user quotas in a view.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**num_users_above_alert_threshold** | **int, none_type** | Number of users who has exceeded their specified alert limit. | [optional] 
**num_users_above_hard_limit** | **int, none_type** | Number of users who has exceeded their specified quota hard limit. | [optional] 
**total_num_users** | **int, none_type** | Total number of users who has either a user quota policy override specified or has non-zero logical usage. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


