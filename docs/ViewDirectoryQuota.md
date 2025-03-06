# ViewDirectoryQuota

Specifies a View directory quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_path** | **str** | Specifies the directory path. | 
**directory_walk_pending** | **bool** | Specifies whether directory quota walk is pending. | [optional] [readonly] 
**quota_policy** | [**ViewDirectoryQuotaPolicy**](ViewDirectoryQuotaPolicy.md) |  | 
**usage_bytes** | **int** | Specifies the directory usage in bytes. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.view_directory_quota import ViewDirectoryQuota

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDirectoryQuota from a JSON string
view_directory_quota_instance = ViewDirectoryQuota.from_json(json)
# print the JSON string representation of the object
print(ViewDirectoryQuota.to_json())

# convert the object into a dict
view_directory_quota_dict = view_directory_quota_instance.to_dict()
# create an instance of ViewDirectoryQuota from a dict
view_directory_quota_from_dict = ViewDirectoryQuota.from_dict(view_directory_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


