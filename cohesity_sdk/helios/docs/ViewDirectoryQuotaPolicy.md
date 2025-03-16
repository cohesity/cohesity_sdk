# ViewDirectoryQuotaPolicy

Specifies a quota for View directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_limit_bytes** | **int** | Specifies if an alert should be triggered when the usage of this resource exceeds this quota limit. This limit is optional and is specified in bytes. If no value is specified, there is no limit. | [optional] 
**hard_limit_bytes** | **int** | Specifies an optional quota limit on the usage allowed for this resource. This limit is specified in bytes. If no value is specified, there is no limit. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_directory_quota_policy import ViewDirectoryQuotaPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDirectoryQuotaPolicy from a JSON string
view_directory_quota_policy_instance = ViewDirectoryQuotaPolicy.from_json(json)
# print the JSON string representation of the object
print(ViewDirectoryQuotaPolicy.to_json())

# convert the object into a dict
view_directory_quota_policy_dict = view_directory_quota_policy_instance.to_dict()
# create an instance of ViewDirectoryQuotaPolicy from a dict
view_directory_quota_policy_from_dict = ViewDirectoryQuotaPolicy.from_dict(view_directory_quota_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


