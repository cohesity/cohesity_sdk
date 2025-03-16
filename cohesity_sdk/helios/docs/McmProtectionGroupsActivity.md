# McmProtectionGroupsActivity

Specifies the Protection Group activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**List[McmProtectionGroupActivity]**](McmProtectionGroupActivity.md) | Specifies the activity list. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_protection_groups_activity import McmProtectionGroupsActivity

# TODO update the JSON string below
json = "{}"
# create an instance of McmProtectionGroupsActivity from a JSON string
mcm_protection_groups_activity_instance = McmProtectionGroupsActivity.from_json(json)
# print the JSON string representation of the object
print(McmProtectionGroupsActivity.to_json())

# convert the object into a dict
mcm_protection_groups_activity_dict = mcm_protection_groups_activity_instance.to_dict()
# create an instance of McmProtectionGroupsActivity from a dict
mcm_protection_groups_activity_from_dict = McmProtectionGroupsActivity.from_dict(mcm_protection_groups_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


