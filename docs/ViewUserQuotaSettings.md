# ViewUserQuotaSettings

Specifies the user quota config on the View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**enabled** | **bool** | Specifies whether user quota is enabled for the View. | 

## Example

```python
from cohesity_sdk.models.view_user_quota_settings import ViewUserQuotaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ViewUserQuotaSettings from a JSON string
view_user_quota_settings_instance = ViewUserQuotaSettings.from_json(json)
# print the JSON string representation of the object
print(ViewUserQuotaSettings.to_json())

# convert the object into a dict
view_user_quota_settings_dict = view_user_quota_settings_instance.to_dict()
# create an instance of ViewUserQuotaSettings from a dict
view_user_quota_settings_from_dict = ViewUserQuotaSettings.from_dict(view_user_quota_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


