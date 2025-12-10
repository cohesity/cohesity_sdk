# UserQuotaSummaryForView

Specifies summary for user quotas in a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**num_users_above_alert_threshold** | **int** | Number of users who has exceeded their specified alert limit. | [optional] 
**num_users_above_hard_limit** | **int** | Number of users who has exceeded their specified quota hard limit. | [optional] 
**total_num_users** | **int** | Total number of users who has either a user quota policy override specified or has non-zero logical usage. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.user_quota_summary_for_view import UserQuotaSummaryForView

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuotaSummaryForView from a JSON string
user_quota_summary_for_view_instance = UserQuotaSummaryForView.from_json(json)
# print the JSON string representation of the object
print(UserQuotaSummaryForView.to_json())

# convert the object into a dict
user_quota_summary_for_view_dict = user_quota_summary_for_view_instance.to_dict()
# create an instance of UserQuotaSummaryForView from a dict
user_quota_summary_for_view_from_dict = UserQuotaSummaryForView.from_dict(user_quota_summary_for_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


