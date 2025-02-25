# ViewUserQuotas

Specifies the default logical user quota on the View along with the list of logical quota overrides for each user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether user quota is enabled for the View. | 
**user_quotas** | [**[UserQuota], none_type**](UserQuota.md) | Array of UserQuota. Specifies the list of UserQuota for each user. | 
**default_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**cookie** | **str, none_type** | Specifies the pagination cookie. | [optional] 
**override_existing_per_user_quotas** | **bool, none_type** | By default, the overrides specified in userQuotas is treated as delta and the existing overrides will be left untouched. Set this to true, if the existing overrides should be cleared before applying overrides specified in userQuotas. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


