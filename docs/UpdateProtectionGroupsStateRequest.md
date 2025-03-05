# UpdateProtectionGroupsStateRequest

Specifies the parameters to perform an action of list of Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action to be performed on all the specfied Protection Groups. &#39;kActivate&#39; specifies that Protection Group should be activated. &#39;kDeactivate&#39; sepcifies that Protection Group should be deactivated. &#39;kPause&#39; specifies that Protection Group should be paused. &#39;kResume&#39; specifies that Protection Group should be resumed. | 
**ids** | **List[str]** | Specifies a list of Protection Group ids for which the state should change. | 

## Example

```python
from cohesity_sdk.models.update_protection_groups_state_request import UpdateProtectionGroupsStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectionGroupsStateRequest from a JSON string
update_protection_groups_state_request_instance = UpdateProtectionGroupsStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectionGroupsStateRequest.to_json())

# convert the object into a dict
update_protection_groups_state_request_dict = update_protection_groups_state_request_instance.to_dict()
# create an instance of UpdateProtectionGroupsStateRequest from a dict
update_protection_groups_state_request_from_dict = UpdateProtectionGroupsStateRequest.from_dict(update_protection_groups_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


