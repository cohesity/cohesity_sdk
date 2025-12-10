# CommonO365RestoreExclusionPolicy

Specifies the common filter policy to be applied for item exclusions in Microsoft 365 restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_after_time_secs** | **int** | Any items after this time will be excluded from restore. The time is specified as number of seconds after snapshot time. | [optional] 
**exclude_all** | **bool** | All items will be excluded from restore. | [optional] 
**exclude_before_time_secs** | **int** | Any items before this time will be excluded from restore. The time is specified as number of seconds before snapshot time. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_o365_restore_exclusion_policy import CommonO365RestoreExclusionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CommonO365RestoreExclusionPolicy from a JSON string
common_o365_restore_exclusion_policy_instance = CommonO365RestoreExclusionPolicy.from_json(json)
# print the JSON string representation of the object
print(CommonO365RestoreExclusionPolicy.to_json())

# convert the object into a dict
common_o365_restore_exclusion_policy_dict = common_o365_restore_exclusion_policy_instance.to_dict()
# create an instance of CommonO365RestoreExclusionPolicy from a dict
common_o365_restore_exclusion_policy_from_dict = CommonO365RestoreExclusionPolicy.from_dict(common_o365_restore_exclusion_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


