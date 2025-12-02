# CommonFilterPolicy

Specifies the filter policy for filtering an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office365_restore_exclusion_policy** | [**O365RestoreExclusionPolicy**](O365RestoreExclusionPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_filter_policy import CommonFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CommonFilterPolicy from a JSON string
common_filter_policy_instance = CommonFilterPolicy.from_json(json)
# print the JSON string representation of the object
print(CommonFilterPolicy.to_json())

# convert the object into a dict
common_filter_policy_dict = common_filter_policy_instance.to_dict()
# create an instance of CommonFilterPolicy from a dict
common_filter_policy_from_dict = CommonFilterPolicy.from_dict(common_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


