# UserQuotaDeleteParams

Specifies list of users to delete logical user quota. If userIds are not specified, all the user quotas will be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | [**List[UserId]**](UserId.md) | Array of userIds. Specifies the list of user Ids to delete logical user quota override. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.user_quota_delete_params import UserQuotaDeleteParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuotaDeleteParams from a JSON string
user_quota_delete_params_instance = UserQuotaDeleteParams.from_json(json)
# print the JSON string representation of the object
print(UserQuotaDeleteParams.to_json())

# convert the object into a dict
user_quota_delete_params_dict = user_quota_delete_params_instance.to_dict()
# create an instance of UserQuotaDeleteParams from a dict
user_quota_delete_params_from_dict = UserQuotaDeleteParams.from_dict(user_quota_delete_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


