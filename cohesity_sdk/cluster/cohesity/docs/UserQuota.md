# UserQuota

Specifies a user quota for a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies the domain name of the user, where the principal&#39; account is maintained. | [optional] 
**sid** | **str, none_type** | Specifies the user sid. | [optional] 
**unix_uid** | **int, none_type** | Specifies the unix Uid. | [optional] 
**user_name** | **str, none_type** | Specifies the full name of the user | [optional] 
**quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**usage_bytes** | **int, none_type** | Specifies the user usage in bytes. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


