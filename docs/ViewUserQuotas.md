# ViewUserQuotas

Specifies the default logical user quota on the View along with the list of logical quota overrides for each user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**enabled** | **bool** | Specifies whether user quota is enabled for the View. | 
**cookie** | **str** | Specifies the pagination cookie. | [optional] 
**override_existing_per_user_quotas** | **bool** | By default, the overrides specified in userQuotas is treated as delta and the existing overrides will be left untouched. Set this to true, if the existing overrides should be cleared before applying overrides specified in userQuotas. | [optional] 
**user_quotas** | [**List[UserQuota]**](UserQuota.md) | Array of UserQuota. Specifies the list of UserQuota for each user. | 

## Example

```python
from cohesity_sdk.models.view_user_quotas import ViewUserQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of ViewUserQuotas from a JSON string
view_user_quotas_instance = ViewUserQuotas.from_json(json)
# print the JSON string representation of the object
print(ViewUserQuotas.to_json())

# convert the object into a dict
view_user_quotas_dict = view_user_quotas_instance.to_dict()
# create an instance of ViewUserQuotas from a dict
view_user_quotas_from_dict = ViewUserQuotas.from_dict(view_user_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


