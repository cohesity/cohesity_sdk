# UserQuotaOverrides

Specifies a list of user quotas set on the View. These user quotas will override the default View user quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | Specifies the pagination cookie. | [optional] 
**override_existing_per_user_quotas** | **bool** | By default, the overrides specified in userQuotas is treated as delta and the existing overrides will be left untouched. Set this to true, if the existing overrides should be cleared before applying overrides specified in userQuotas. | [optional] 
**user_quotas** | [**List[UserQuota]**](UserQuota.md) | Array of UserQuota. Specifies the list of UserQuota for each user. | 

## Example

```python
from cohesity_sdk.models.user_quota_overrides import UserQuotaOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuotaOverrides from a JSON string
user_quota_overrides_instance = UserQuotaOverrides.from_json(json)
# print the JSON string representation of the object
print(UserQuotaOverrides.to_json())

# convert the object into a dict
user_quota_overrides_dict = user_quota_overrides_instance.to_dict()
# create an instance of UserQuotaOverrides from a dict
user_quota_overrides_from_dict = UserQuotaOverrides.from_dict(user_quota_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


